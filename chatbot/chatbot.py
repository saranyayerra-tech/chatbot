def chatbot():
    print("🤖 Welcome to the Basic Chatbot!")
    print("Type 'bye' to exit.\n")
    while True:
        user = input("You: ").lower()
        if user == "hello":
            print("Bot: Hi! How are you?")
        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")
        elif user == "i am fine":
            print("Bot: That's great to hear!")
        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")
        elif user == "ok bye":
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")
chatbot()