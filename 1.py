import openai

# Set your OpenAI API key here
openai.api_key = "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"

# Define bot responses
bot_responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm just a computer program, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "how can you help": "I can help with a wide range of topics, from answering questions to providing information.",
    "what's your purpose": "I'm here to provide information, answer questions, and assist with various tasks.",
    "thank you": "You're welcome! Feel free to ask if you need more help.",
    "tell me a joke": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
    "what's the weather like": "I'm afraid I can't provide real-time information, but you can check a weather website or app.",
    "who created you": "I was created by UniVerse Ai Founded By Satyam Singh using their LLaVa technology.",
    "can you recommend a book": "Of course! What genre are you interested in? Fiction, non-fiction, sci-fi, fantasy?",
    "how do I reset my password": "To reset your password, you'll usually need to visit the login page and look for the 'Forgot Password' option.",
    "default": "I'm not sure how to respond to that."
}

# Main interaction loop
print("🌋 LLaVA: Large Language Virtual Assistant")
print()
print("Welcome To LLaVa")

name=input("Enter Your Name ")

print("Hi "+name+"\nGood Afternoon\nHow Can I Help You")
while True:
    user_input = input("You: ").lower()

    # Check if user wants to exit
    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    # Check if llm should respond
    if user_input not in bot_responses:
        llm_response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine for GPT-3.5
            prompt=user_input,
            max_tokens=50
        )
        print("Bot (llm):", llm_response.choices[0].text.strip())
    else:
        print("Bot:", bot_responses[user_input])
