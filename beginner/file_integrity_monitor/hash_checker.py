import hashlib
import os
file = input("Enter the full path to the file (or ensure the file is in the current directory): ")
hash_file = input("Enter the full path to the hash file (or ensure the file is in the current directory): ")

# Function to check if both files exist and create attempt to create hash file if it does not exist
def check_files_exist(file_path, hash_file_path):
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return False
    if not os.path.isfile(hash_file_path):
        print(f"Error: The hash file '{hash_file_path}' does not exist.")
        print("Creating hash file...")
        try:
            with open(hash_file_path, "w") as f:
                pass  # Create an empty hash file
            print(f"Hash file '{hash_file_path}' created successfully.")
        except Exception as e:
            print(f"Error creating hash file: {e}")
            print("Please manually create the hash file and try again.")
        return False
    return True

# Function to check add hash values to the hash file
def append_hash(hash,file_path, hash_file_path):
    try:
        with open(hash_file_path, "a") as hash_file:
            hash_file.write(f"{file_path} : {hash}\n")
        print(f"Hash value '{hash}' appended to '{hash_file_path}'.")
    except Exception as e:
        print(f"Error writing to hash file: {e}")

try:
    with open(file, "rb") as f:
        # Read the file in chunks to avoid memory issues with large files
        chunk_size = 8192
        hasher = hashlib.sha256()

        while chunk := f.read(chunk_size):
            hasher.update(chunk)

        # Get the hexadecimal digest of the hash
        sha256_hash = hasher.hexdigest()
        print(f"SHA-256: {sha256_hash}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Check if both files exist
check_files_exist(file, hash_file)

# Append the hash value to the hash file
if check_files_exist(file, hash_file):
    append_hash(sha256_hash, file, hash_file)