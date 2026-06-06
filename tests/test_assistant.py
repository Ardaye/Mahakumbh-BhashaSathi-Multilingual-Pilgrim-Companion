import unittest
from maha_kumbh_assistant import build_translation, choose_answer, normalize_language


class PilgrimAssistantTests(unittest.TestCase):
    def test_translate_phrase_english_to_hindi(self):
        result = build_translation('Translate thank you to Hindi', 'English')
        self.assertEqual(result, 'धन्यवाद')

    def test_translate_phrase_english_to_french(self):
        result = build_translation('Translate hello to French', 'English')
        self.assertEqual(result, 'Bonjour')

    def test_translate_phrase_english_to_german(self):
        result = build_translation('Translate thank you to German', 'English')
        self.assertEqual(result, 'Danke')

    def test_translate_phrase_english_to_japanese(self):
        result = build_translation('Translate please to Japanese', 'English')
        self.assertEqual(result, 'お願いします')

    def test_translate_phrase_english_to_marathi(self):
        result = build_translation('Translate hello to Marathi', 'English')
        self.assertEqual(result, 'नमस्कार')

    def test_translate_phrase_missing_language(self):
        result = build_translation('Translate hello to Spanish', 'English')
        self.assertTrue('not available' in result)

    def test_navigation_answer(self):
        result = choose_answer('Where is the main gate?', 'English')
        self.assertIn('main gate', result.lower())

    def test_emergency_answer(self):
        result = choose_answer('I need urgent help', 'English')
        self.assertIn('call 100', result)

    def test_women_helpline_answer(self):
        result = choose_answer('What is the women helpline number?', 'English')
        self.assertEqual(result, 'For women-specific assistance, call 1091, the women’s helpline at the Mahakumbh site.')

    def test_normalize_language_falls_back_to_english(self):
        self.assertEqual(normalize_language('spanish'), 'English')
        self.assertEqual(normalize_language('hindi'), 'Hindi')


if __name__ == '__main__':
    unittest.main()
