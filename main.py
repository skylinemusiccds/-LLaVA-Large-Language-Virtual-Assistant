import replicate as r

api_token="r8_ZW7dpCvq2cOIyGtEY01JzLqakH7n1re4QT7fx"

r.client(api_token)

r.run("stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
input={"prompt":""})

#['https://replicate.com/api/models/stability-ai/stable-diffusion/files/50fcac81-865d-499e-81ac-49de0cb79264/out-0.png']






'''from transformers import GPT3Tokenizer, GPT3LMHeadModel

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

# Load tokenizer and model

tokenizer = GPT3Tokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
model = GPT3LMHeadModel.from_pretrained("EleutherAI/gpt-neo-2.7B")

# Main interaction loop

print("🌋 LLaVA: Large Language Virtual Assistant")
print()
print("Welcome To LLaVa")

name = input("Enter Your Name ")

print("Hi " + name + "\nGood Afternoon\nHow Can I Help You")
while True:
    user_input = input("You: ").lower()

    # Check if user wants to exit
    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    # Check if predefined bot response exists
    if user_input in bot_responses:
        print("Bot:", bot_responses[user_input])
    else:
        # Use the Hugging Face model to generate a response
        input_ids = tokenizer.encode(user_input, return_tensors="pt")
        with torch.no_grad():
            output = model.generate(input_ids, max_length=50, num_return_sequences=1)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        print("Bot (Hugging Face):", response)'''


