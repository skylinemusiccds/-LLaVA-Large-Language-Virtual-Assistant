import replicate 
import gradio as gr
from getpass import getpass
import os


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
# get a token: https://replicate.com/account


#REPLICATE_API_TOKEN = getpass()
os.environ["REPLICATE_API_TOKEN"] = 'r8_6y1r03mreETjEJALHFCGfWAKzTbCF9r0Rv5sj'
# Main interaction loop

print("🌋 LLaVA: Large Language Virtual Assistant")
print()
print("Welcome To LLaVa")

#name = input("Enter Your Name ")

print("Hi \nGood Evening\nHow Can I Help You")
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
        iterator = replicate.run("replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5",input={"prompt":user_input })
    for text in iterator:
        print(text,end="")
      
      
      
      
      
'''input_ids = tokenizer.encode(user_input, return_tensors="pt")
        with torch.no_grad():
            output = model.generate(input_ids, max_length=50, num_return_sequences=1)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        print("Bot (Hugging Face):", response)'''
