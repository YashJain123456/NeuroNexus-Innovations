import re

def simple_chatbot(user_input):
    # Define patterns and corresponding responses
    patterns_and_responses = {
        r"(hi|hello|hey)( there)?": "Hi! How can I help you?",
        r"how are you": "I'm just a computer program, but thanks for asking!",
        r"what is your name": "I'm a chatbot created by OpenAI. You can call me ChatGPT.",
        r"bye|goodbye": "Goodbye! If you have more questions, feel free to ask.",
        r"(\d+) (plus|minus|times|multiplied by|divided by) (\d+)": lambda m: perform_math_operation(m.group(1), m.group(2), m.group(3)),
        r"thanks|thank you": "You're welcome!",
        # Add more patterns and responses as needed
    }

    # Check each pattern and respond if there's a match
    for pattern, response in patterns_and_responses.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            if callable(response):
                return response(match)
            else:
                return response

    # If no match, respond with a default message
    return "I'm sorry, I don't understand that. Can you please rephrase or ask another question?"

def perform_math_operation(num1, operator, num2):
    num1, num2 = float(num1), float(num2)
    if operator.lower() == "plus":
        return f"{num1} + {num2} = {num1 + num2}"
    elif operator.lower() == "minus":
        return f"{num1} - {num2} = {num1 - num2}"
    elif operator.lower() in ["times", "multiplied by"]:
        return f"{num1} * {num2} = {num1 * num2}"
    elif operator.lower() in ["divided by"]:
        if num2 != 0:
            return f"{num1} / {num2} = {num1 / num2}"
        else:
            return "Cannot divide by zero."

# Main loop to interact with the chatbot
print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
