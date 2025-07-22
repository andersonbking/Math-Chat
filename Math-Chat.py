import random
import re

print("Welcome! Type a greeting, a math expression, or enter something. Type 'quit', 'exit', or 'stop' to end.")

while True:
    user_input = input("Enter something: ").strip().lower()

    greetings = ["hello", "hi", "hola", "howdy", "what's up", "hey"]
    farewells = ["peace", "bye", "chao"]
    quit_commands = ["quit", "exit", "stop"]
    help_commands = ["help", "aid", "i", "?"]
    
    # List of possible random responses for greetings
    greeting_responses = [
        "Hi there!",
        "Hello!",
        "Hey!",
        "Greetings!",
        "Howdy!",
        "What's up?",
        "Hey, good to see you!"
    ]

    # Regular expression to detect basic math expressions
    math_pattern = r'^[\d\s\+\-\*/\^\(\)\.]+$'

    if user_input == "" or user_input in greetings:
        # Pick and print a random greeting response
        print(random.choice(greeting_responses))
    elif user_input in help_commands:
        print("How can I help you? You can type greetings, math expressions (e.g., '2 + 2'), or 'quit' to exit.")
    elif user_input in farewells:
        response = input("Bye! Do you wish to exit? (yes/no): ").strip().lower()
        if response == "yes":
            print("Farewell!")
            break
    elif user_input in quit_commands:
        print("Stopping the program. Goodbye!")
        break
    elif re.match(math_pattern, user_input):
        try:
            # Evaluate the math expression
            result = eval(user_input, {"__builtins__": {}}, {"pow": pow})
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error evaluating math expression: {e}. Please try a valid expression like '2 + 2' or '3 * 4'.")
    else:
        print("I didn't understand that. Try a greeting, a math expression, or type 'help' for assistance.")

