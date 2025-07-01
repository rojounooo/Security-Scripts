"""
Filename: maxmind_setup.py
Author: rojounooo
Created: 2025-06-30
Last Updated: 2025-07-01

Description:
This script downloads and extracts the MaxMind GeoLite2 City database.
It is designed to be cross-platform and works on both Windows and Linux.
It requires a valid MaxMind license key to download the database which can be obtained from MaxMind's website after creating an account.
It will also need a valid edition ID, which is typically "GeoLite2-City" for the city database.
Make sure to set your MaxMind license key in the environment variable MAXMIND_LICENSE_KEY
or replace the fallback placeholder below.
"""

import requests
import tarfile
import os
import platform
import sys

# === Configuration ===
LICENSE_KEY = "your_license_key_here"  # Replace with your actual MaxMind license key
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
def safe_filter(tarinfo):
    # Prevent absolute paths
    if tarinfo.name.startswith('/'):
        print(f"Skipping absolute path: {tarinfo.name}")
        return None
    # Prevent path traversal
    if '..' in tarinfo.name.split(os.path.sep):
        print(f"Skipping path traversal file: {tarinfo.name}")
        return None
    return tarinfo

def extract_database():
    print("Extracting database...")
    with tarfile.open(TAR_FILENAME, 'r:gz') as tar:
        tar.extractall(path=EXTRACT_DIR, filter=safe_filter)
    print("Extraction complete.")

# === Cleanup ===
def cleanup(remove_script=False):
    print("Cleaning up temporary files...")
    if os.path.exists(TAR_FILENAME):
        os.remove(TAR_FILENAME)
        print(f"Removed temporary file: {TAR_FILENAME}")
    else:
        print(f"File {TAR_FILENAME} does not exist, skipping cleanup.")

    if remove_script:
        script_path = os.path.realpath(__file__)
        try:
            os.remove(script_path)
            print(f"Removed setup script: {script_path}")
        except Exception as e:
            print(f"Failed to remove setup script: {e}")

# === Run ===
def main():
    print(f"Running on: {platform.system()}")
    if LICENSE_KEY == "your_license_key_here":
        print("ERROR: Please set your MaxMind license key.")
        sys.exit(1)
    try:
        download_database()
        extract_database()
    except Exception as e:
        print("Error occurred:", e)
        sys.exit(1)
    cleanup(remove_script=False)  # Set to True if you want to delete the script after running

if __name__ == "__main__":
    main()
# This script is designed to be run once to set up the MaxMind GeoLite2 City database.