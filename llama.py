import requests

# Set up the LLaMA API endpoint and API key
url = "https://api.llamabot.io/v1/models/model-1"
api_key = "YOUR_API_KEY"

# Set up the question and response parameters
question = "What is the capital of France?"
response = None

# Make a POST request to the LLaMA API with the question and API key
response = requests.post(url, headers={"Content-Type": "application/json"}, data={"input": question, "api_key": api_key})

# Check if the response was successful
if response.status_code == 200:
    # Extract the response text from the JSON response
    response_text = response.json()["output"]
    print(response_text)
else:
    print("Error:", response.status_code)