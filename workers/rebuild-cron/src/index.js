const ROME_TIME_ZONE = "Europe/Rome";
const FIRST_BUILD_HOUR = 5;
const LAST_BUILD_HOUR = 22;

/**
 * Return the hour represented by a scheduled UTC timestamp in Europe/Rome.
 * The decision intentionally uses ScheduledController.scheduledTime rather
 * than the actual execution time, which may be delayed by the platform.
 *
 * @param {number} scheduledTime
 * @returns {number}
 */
export function getRomeHour(scheduledTime) {
  const formattedHour = new Intl.DateTimeFormat("en-GB", {
    timeZone: ROME_TIME_ZONE,
    hour: "2-digit",
    hourCycle: "h23"
  }).format(new Date(scheduledTime));

  return Number.parseInt(formattedHour, 10);
}

/**
 * @param {number} scheduledTime
 * @returns {boolean}
 */
export function isBuildWindow(scheduledTime) {
  const localHour = getRomeHour(scheduledTime);
  return localHour >= FIRST_BUILD_HOUR && localHour <= LAST_BUILD_HOUR;
}

/**
 * @typedef {{
 *   success?: unknown,
 *   result?: {
 *     build_uuid?: unknown,
 *     already_exists?: unknown,
 *     status?: unknown
 *   } | null
 * }} DeployHookPayload
 */

/**
 * Trigger Workers Builds and validate both the HTTP response and the API
 * envelope. The hook URL is deliberately never included in errors or logs.
 *
 * @param {string} hookUrl
 * @param {typeof fetch} fetchImpl
 * @returns {Promise<{buildUuid: string, alreadyExists: boolean, status: string | null}>}
 */
export async function triggerBuild(hookUrl, fetchImpl = fetch) {
  const response = await fetchImpl(hookUrl, {
    method: "POST",
    headers: { Accept: "application/json" }
  });

  if (!response.ok) {
    throw new Error(`Deploy Hook HTTP ${response.status}`);
  }

  /** @type {DeployHookPayload} */
  let payload;
  try {
    payload = await response.json();
  } catch {
    throw new Error("Deploy Hook returned malformed JSON");
  }

  const result = payload && typeof payload === "object" ? payload.result : null;
  if (
    payload?.success !== true ||
    !result ||
    typeof result !== "object" ||
    typeof result.build_uuid !== "string" ||
    result.build_uuid.length === 0
  ) {
    throw new Error("Deploy Hook returned an invalid success payload");
  }

  return {
    buildUuid: result.build_uuid,
    alreadyExists: result.already_exists === true,
    status: typeof result.status === "string" ? result.status : null
  };
}

/** @type {ExportedHandler<Env>} */
const worker = {
  async scheduled(event, env) {
    const localHour = getRomeHour(event.scheduledTime);

    if (!isBuildWindow(event.scheduledTime)) {
      console.log(JSON.stringify({
        message: "scheduled build skipped",
        scheduledTime: event.scheduledTime,
        timeZone: ROME_TIME_ZONE,
        localHour
      }));
      return;
    }

    try {
      const build = await triggerBuild(env.DEPLOY_HOOK_URL);
      console.log(JSON.stringify({
        message: "scheduled build requested",
        scheduledTime: event.scheduledTime,
        timeZone: ROME_TIME_ZONE,
        localHour,
        build_uuid: build.buildUuid,
        already_exists: build.alreadyExists,
        status: build.status
      }));
    } catch (error) {
      console.error(JSON.stringify({
        message: "scheduled build request failed",
        scheduledTime: event.scheduledTime,
        timeZone: ROME_TIME_ZONE,
        localHour,
        error: error instanceof Error ? error.message : String(error)
      }));
      throw error;
    }
  }
};

export default worker;
