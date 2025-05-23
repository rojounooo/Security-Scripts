import hashlib

file = input("Enter the file name: ")

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
