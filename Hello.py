print("Hello, World!")
input("Press Enter to exit...")

import requests

# GitHub raw file URL (Replace with your actual repo and username)
url = "https://raw.githubusercontent.com/sasinthanapro/University/main/hello.py"

# Fetch the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("File fetched successfully!\n")
    print(response.text)  # Print the file contents
else:
    print("Failed to fetch the file. Status code:", response.status_code)


