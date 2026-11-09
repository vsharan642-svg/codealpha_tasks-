
import datetime

print("=" * 50)
print("             PYTHON CHATBOT    ")
print("=" * 50)

print("Bot: Hello! Welcome to Python Chatbot.")
print("Bot: I am here to chat with you.")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' to end the conversation.")

name = ""

while True:

    user_input = input("\nYou: ").strip().lower()

    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        print("Bot: Hello! Nice to meet you.")

    elif user_input.startswith("my name is"):
        name = user_input[11:].strip().title()

        if name:
            print("Bot: Nice to meet you, " + name + "!")
        else:
            print("Bot: Please tell me your name.")

    elif user_input == "what is my name":
        if name:
            print("Bot: Your name is " + name + ".")
        else:
            print("Bot: You haven't told me your name yet.")

    elif user_input == "how are you":
        print("Bot: I am doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif user_input == "who created you":
        print("Bot: I was created using Python programming.")

    elif user_input == "what can you do":
        print("Bot: I can greet you, answer basic questions,")
        print("     tell the time and date, and remember your name.")

    elif user_input == "time" or user_input == "what is the time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is " + current_time)

    elif user_input == "date" or user_input == "what is today's date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is " + current_date)

    elif user_input == "help":
        print("\nBot: Here are some commands you can try:")
        print("     hello")
        print("     how are you")
        print("     my name is Sharan")
        print("     what is my name")
        print("     what is your name")
        print("     who created you")
        print("     what can you do")
        print("     time")
        print("     date")
        print("     bye")

    elif user_input == "thanks" or user_input == "thank you":
        print("Bot: You're welcome!")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! Have a wonderful day!")
        break

    elif user_input == "":
        print("Bot: Please enter something.")

    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see available commands.")

print("\n" + "=" * 50)
print("        CHAT SESSION ENDED")
print("=" * 50)
