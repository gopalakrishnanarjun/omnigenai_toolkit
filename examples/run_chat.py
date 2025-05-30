from omnigenai_toolkit.chatbot import SmartAIChatbot

def main():
    bot = SmartAIChatbot()
    print("SmartAI Chatbot (type 'bye' or 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print("Bot:", bot.respond(user_input))
            break
        response = bot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
