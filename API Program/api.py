import requests

# Joke API URL
url = "https://official-joke-api.appspot.com/random_joke"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    joke = response.json()
    
    # Display the joke
    print("Here's a random joke for you!")
    print(f"Q: {joke['setup']}")
    print(f"A: {joke['punchline']}")
else:
    print("Failed to fetch joke. Error Code:", response.status_code)