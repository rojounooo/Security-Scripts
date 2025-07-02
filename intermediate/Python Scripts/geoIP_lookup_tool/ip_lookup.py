"""
Filename: ip_lookup.py
Author: rojounooo
Created: 30-06-2025
Last Updated: 02-07-2025

Description:
This script performs GeoIP lookups for a single IP address or a list of IP addresses using a local MaxMind GeoLite2 database.
"""

# === Import Libraries ===
import os  # For file path operations (optional here)
import sys  # For system-specific functions like exit()
import argparse  # For command-line argument parsing
import geoip2.database  # For GeoIP database reader

# === Command Line Argument Parsing ===
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="This script will take a single IP or a list of IP addresses and perform a lookup using a local MaxMind database."
    ) # Small description of the script's functionality

    group = parser.add_mutually_exclusive_group(required=True) # Either a single IP or a list must be provided 

    # Adding arguments for single IP or list of IPs
    group.add_argument("--single", type=str, help="Single IP address")
    group.add_argument("--list", type=str, help="Path to list of IP addresses")

    args = parser.parse_args() # Parse the command line arguments

    if args.single:
        return [args.single] # If a single IP is provided, return it as a list
    elif args.list:
        try:
            with open(args.list, 'r') as file:
                return [line.strip() for line in file if line.strip()] # Read lines from the file, stripping whitespace and ignoring empty lines
        except FileNotFoundError:
            print(f"[!] File '{args.list}' not found.") # Exit if the file does not exist
            sys.exit(1)

# === Load GeoIP Database ===
def load_geoip_database(db_path):
    try:
        return geoip2.database.Reader(db_path) # Load the GeoIP database from the specified path
    
    except Exception as e:
        print(f"[!] Error loading GeoIP database: {e}") # Exit if there is an error loading the database
        sys.exit(1)

# === Perform Lookup ===
def lookup_ip(reader, ip_address):
    try:
        response = reader.city(ip_address) # Perform the lookup for the given IP address
        print(f"IP Address: {ip_address}") # Display the IP address being looked up
        print(f"Country: {response.country.name} ({response.country.iso_code})") # Display the country name and ISO code
        print(f"Region: {response.subdivisions.most_specific.name} ({response.subdivisions.most_specific.iso_code})") # Display the region name and ISO code
        print(f"City: {response.city.name}") # Display the city name
        print(f"Latitude: {response.location.latitude}, Longitude: {response.location.longitude}") # Display the latitude and longitude
    
    except geoip2.errors.AddressNotFoundError:
        print(f"[!] IP address '{ip_address}' not found in the database.") # Handle case where IP address is not found in the database
    
    except Exception as e:
        print(f"[!] Error looking up IP address '{ip_address}': {e}") # Handle any other errors that may occur during the lookup

# === Main Function ===
def main():
    print("GeoIP Lookup Tool")
    print("==================")

    # Get IPs from CLI args
    ip_addresses = parse_arguments()

    # Path to your GeoLite2 database file (adjust as needed)
    db_path = "GeoLite2-City.mmdb"

    # Load the database
    reader = load_geoip_database(db_path)

    # Perform lookup for each IP
    for ip in ip_addresses:
        lookup_ip(reader, ip)
        print("-" * 40)

    reader.close()

# === Run the Script ===
if __name__ == "__main__":
    main()
