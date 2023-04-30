#only look if you have a clue on what youre doing. this uses a 500k word list and checks them all, it doesnt work very well tho
import requests

# Set the file paths for the input and output files
input_file_path = "C:/Users/*****/Documents/words.txt"
output_file_path = "C:/Users/*****/Documents/available_usernames2.txt"

# Create an empty list to store available usernames
available_usernames = []

# Open the dictionary file and read its contents
with open(input_file_path, "r") as f:
    # Read each line of the file as a separate word
    words = [word.strip() for word in f.readlines()]

# Loop through each word in the dictionary
for word in words:
    # Check if the word contains any characters that are not allowed in Minecraft usernames
    if not all(char.isalnum() or char in "_-" for char in word):
        continue
        
    # Construct the URL with the username
    url = f'https://api.mojang.com/users/profiles/minecraft/{word}'

    # Make a GET request to the URL
    response = requests.get(url)

    # Check the response status code to determine availability
    if response.status_code == 200:
        print(f"Username {word} is not available")
    else:
        print(f"Username {word} is available!")
        available_usernames.append(word)

# Write the list of available usernames to a file
with open(output_file_path, "w") as f:
    f.write("\n".join(available_usernames))
