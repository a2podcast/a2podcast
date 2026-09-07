#!/usr/bin/env python3
"""Unit tests for ingest helpers that do not access the network or filesystem."""

import unittest

try:
    from scripts.ingest import extract_description
except ModuleNotFoundError:  # Support direct execution from the project root.
    from ingest import extract_description


class ExtractDescriptionTests(unittest.TestCase):
    def test_cleans_markdown_and_urls(self):
        raw = (
            "> Scopri **Comandi Rapidi** nella [guida Apple](https://example.com/guida) "
            "e guarda https://example.com/video. Un percorso pratico e completo.\n\n"
            "Testo successivo che non fa parte della descrizione."
        )

        description = extract_description(raw)

        self.assertEqual(
            description,
            "Scopri Comandi Rapidi nella guida Apple e guarda. Un percorso pratico e completo.",
        )
        self.assertNotIn("http", description)
        self.assertNotRegex(description, r"[*_\[\]]")

    def test_prefers_complete_sentence_within_limit(self):
        first = "Questa introduzione spiega il contesto con esempi concreti e indicazioni utili per orientarsi senza perdere i passaggi essenziali."
        second = " " + "parola " * 40

        description = extract_description(f"> {first}{second}")

        self.assertEqual(description, first)
        self.assertLessEqual(len(description), 300)

    def test_truncates_at_word_boundary_when_sentence_is_too_long(self):
        raw = "> " + "automazione " * 40

        description = extract_description(raw)

        self.assertLessEqual(len(description), 300)
        self.assertTrue(description.endswith("…"))
        self.assertFalse(description.endswith("automaz…"))

    def test_cleans_fallback_when_blockquote_is_missing(self):
        fallback = "Approfondisci _Hazel_ su www.example.com e organizza meglio i documenti."

        description = extract_description("Nessun riassunto qui.", fallback=fallback)

        self.assertEqual(
            description,
            "Approfondisci Hazel su e organizza meglio i documenti.",
        )


if __name__ == "__main__":
    unittest.main()
