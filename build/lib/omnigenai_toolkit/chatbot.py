import re
import random
from datetime import datetime

class SmartAIChatbot:
    def __init__(self):
        self.patterns = [
            (r'hello|hi|hey', [
                "Hello! 👋", "Hi there!", "Hey! How can I help?"
            ]),
            (r'how are you', [
                "I'm doing well, thank you!", "I'm just code, but I'm running fine :)"
            ]),
            (r'what is your name', [
                "I'm SmartAI, your simple Python chatbot.",
                "They call me SmartAI — how can I help you?"
            ]),
            (r'(.*) your name', [
                "Names aren't important. But you can call me SmartAI."
            ]),
            (r'bye|exit', [
                "Goodbye! 👋", "See you later!", "Bye! Take care!"
            ]),
        ]

    def respond(self, user_input):
        user_input = user_input.lower().strip()
        for pattern, responses in self.patterns:
            if re.search(pattern, user_input):
                return random.choice(responses)
        return self.fallback_response(user_input)

    def fallback_response(self, user_input):
        if "weather" in user_input:
            return "Sorry, I can't check the weather without internet access."
        elif "time" in user_input:
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
        return "Hmm... I didn't quite get that. Can you rephrase?"
