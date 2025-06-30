"""
Filename: maxmind_setup.py
Author: rojounooo
Created: 2025-06-30
Last Updated: 2025-06-30

Description:
This script downloads and extracts the MaxMind GeoLite2 City database.
It is designed to be cross-platform and works on both Windows and Linux.
It requires a valid MaxMind license key to download the database which can be obtained from MaxMind's website after creating an account.
It will also need a valid edition ID, which is typically "GeoLite2-City" for the city database.
Make sure to replace `your_license_key_here` with your actual MaxMind license key.
"""


import requests
import tarfile
import os
import platform

# === Configuration ===
LICENSE_KEY = "your_license_key_here"
EDITION_ID = "GeoLite2-City"
DOWNLOAD_URL = f"https://download.maxmind.com/app/geoip_download?edition_id={EDITION_ID}&license_key={LICENSE_KEY}&suffix=tar.gz"
TAR_FILENAME = f"{EDITION_ID}.tar.gz"
EXTRACT_DIR = EDITION_ID

# === Download ===
def download_database():
    print(f"Downloading {EDITION_ID} database...")
    response = requests.get(DOWNLOAD_URL, timeout=30)
    response.raise_for_status()
    with open(TAR_FILENAME, 'wb') as f:
        f.write(response.content)
    print("Download complete.")

# === Extract ===
def extract_database():
    print("Extracting database...")
    with tarfile.open(TAR_FILENAME, 'r:gz') as tar:
        tar.extractall(path=EXTRACT_DIR)
    print("Extraction complete.")

# === Run ===
def main():
    print(f"Running on: {platform.system()}")
    try:
        download_database()
        extract_database()
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
