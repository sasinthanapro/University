import requests

url = "https://github.com/sasinthanapro/University.git/hello.py"
response = requests.get(url)

if response.status_code == 200:
    print("Fetched script content:\n")
    print(response.text)
else:
    print("Failed to fetch the script. Check the URL and repository settings.")
print("Hello, World!")
input("Press Enter to exit...")

