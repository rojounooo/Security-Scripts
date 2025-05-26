# This script can be automated to run periodically and check the hash values against the stored ones in the hash file.

import hashlib
import os

file_path = input("Enter the full path to file (or ensure the file is in the current directory): ")
hash_file = input("Enter the full path to the hash file (or ensure the file is in the current directory): ")

# Function to check if both files_list exist and create attempt to create hash file if it does not exist
def check_files_exist(file_path, hash_file_path):
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return False
    if not os.path.isfile(hash_file_path):
        print(f"Error: The hash file '{hash_file_path}' does not exist.")
        print("Please try again")
        return False
    return True

# Function to generate the hash for a file

def calculate_sha256(file_path):
    with open(file_path, "rb") as f:
        chunk_size = 8192
        hasher = hashlib.sha256()

        while chunk := f.read(chunk_size):
            hasher.update(chunk)

    return hasher.hexdigest()

if not check_files_exist(file_path, hash_file):
    print("Exiting the program due to file existence check failure.")
    exit()
new_path_hash = calculate_sha256(file_path)
paths = []
old_path_hashes = []

# Check hash values to the hash file

with open(hash_file, "r") as f:
    hash_values = f.readlines()
    for line in hash_values:
        path, hash_value = line.strip().split(" : ")
        paths.append(path)
        old_path_hashes.append(hash_value)
    if file_path in paths:
        index = paths.index(file_path)
        if old_path_hashes[index] == new_path_hash:
            print(f"File '{file_path}' is unchanged.")
        else:
            print(f"File '{file_path}' has been modified.")