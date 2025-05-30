import unittest
from omnigenai_toolkit.chatbot import SmartAIChatbot

class TestSmartAIChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = SmartAIChatbot()

    def test_greeting(self):
        self.assertIn(self.bot.respond("hello"), [
            "Hello! 👋", "Hi there!", "Hey! How can I help?"
        ])

    def test_fallback(self):
        self.assertEqual(
            self.bot.respond("tell me a joke"),
            "Hmm... I didn't quite get that. Can you rephrase?"
        )

if __name__ == "__main__":
    unittest.main()
