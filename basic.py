import requests

# List of usernames to check
usernames = ['serotonin', 'doxycycline', 'aspirin', 'ibuprofen', 'paracetamol', 'morphine', 'insulin',]

# Loop through each username in the list
for username in usernames:
    # Construct the URL with the username
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}'

    # Make a GET request to the URL
    response = requests.get(url)

    # Check the response status code to determine availability
    if response.status_code == 200:
        print(f"Username {username} is not available")
    else:
        print(f"Username {username} is available!")
