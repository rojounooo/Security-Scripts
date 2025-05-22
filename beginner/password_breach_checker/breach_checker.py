# This script checks if a password has been compromised in known data breaches using the Have I Been Pwned API.

# Import libraries
import requests
import hashlib

password = input("Enter a password to check if it has been compromised: ")

# Function to hash the password
def hash_password(password):
    # Hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return sha1_hash[:5].upper(), sha1_hash[5:].upper()

# Function to send GET request to the API
def send_request(hashed_password):
    # Send a GET request to the Have I Been Pwned API
    url = f"https://api.pwnedpasswords.com/range/{hashed_password}"
    response = requests.get(url)
    return response

# Function to check if the password has been compromised 
prefix, suffix = hash_password(password)
response = send_request(prefix)
if response.status_code == 200:
    # Check if the password is in the response
    for line in response.text.splitlines():
        returned_suffix, count = line.split(':')
        if returned_suffix == suffix:
            print(f"Your password has been compromised {count} times.")
            break