import unittest
from translator import english_to_french, french_to_english

# Testing the frenchToEnglish function
class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        # Test for the translation of the world 'Hello' and 'Bonjour'.
        self.assertEqual(french_to_english("Bonjour"), "Hello")

# Testing the englishToFrench function
class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        # Test for the translation of the world 'Hello' and 'Bonjour'.
        self.assertEqual(english_to_french("Hello."), "Bonjour.")

if __name__ == "__main__":
    unittest.main()