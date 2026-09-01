import assert from "node:assert/strict";
import test from "node:test";

import { getRomeHour, isBuildWindow, triggerBuild } from "../src/index.js";

const time = (iso) => Date.parse(iso);

test("usa la finestra 05:05–22:05 in Europe/Rome durante CET", () => {
  const cases = [
    ["2026-01-15T03:05:00Z", 4, false],
    ["2026-01-15T04:05:00Z", 5, true],
    ["2026-01-15T21:05:00Z", 22, true],
    ["2026-01-15T22:05:00Z", 23, false]
  ];

  for (const [iso, expectedHour, expectedDecision] of cases) {
    assert.equal(getRomeHour(time(iso)), expectedHour, iso);
    assert.equal(isBuildWindow(time(iso)), expectedDecision, iso);
  }
});

test("usa la finestra 05:05–22:05 in Europe/Rome durante CEST", () => {
  const cases = [
    ["2026-07-15T02:05:00Z", 4, false],
    ["2026-07-15T03:05:00Z", 5, true],
    ["2026-07-15T20:05:00Z", 22, true],
    ["2026-07-15T21:05:00Z", 23, false]
  ];

  for (const [iso, expectedHour, expectedDecision] of cases) {
    assert.equal(getRomeHour(time(iso)), expectedHour, iso);
    assert.equal(isBuildWindow(time(iso)), expectedDecision, iso);
  }
});

test("accetta una risposta Deploy Hook valida", async () => {
  const build = await triggerBuild("https://hook.invalid/secret", async () => new Response(JSON.stringify({
    success: true,
    result: {
      build_uuid: "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      already_exists: false,
      status: "queued"
    }
  }), { status: 200 }));

  assert.deepEqual(build, {
    buildUuid: "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    alreadyExists: false,
    status: "queued"
  });
});

test("registra la deduplicazione già segnalata da Workers Builds", async () => {
  const build = await triggerBuild("https://hook.invalid/secret", async () => new Response(JSON.stringify({
    success: true,
    result: {
      build_uuid: "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      already_exists: true,
      status: "initializing"
    }
  }), { status: 200 }));

  assert.equal(build.alreadyExists, true);
});

for (const status of [400, 404, 500, 503]) {
  test(`rifiuta una risposta HTTP ${status}`, async () => {
    await assert.rejects(
      triggerBuild("https://hook.invalid/secret", async () => new Response("errore", { status })),
      new RegExp(`HTTP ${status}`)
    );
  });
}

test("rifiuta JSON malformato", async () => {
  await assert.rejects(
    triggerBuild("https://hook.invalid/secret", async () => new Response("{", { status: 200 })),
    /malformed JSON/
  );
});

test("rifiuta un envelope success non valido", async () => {
  await assert.rejects(
    triggerBuild("https://hook.invalid/secret", async () => new Response(JSON.stringify({
      success: true,
      result: { already_exists: false }
    }), { status: 200 })),
    /invalid success payload/
  );
});
