# Import Libraries
import geoip2.database # for GeoIP database lookup
from sys import argv # accept IP address from user
import geoip2.errors # for handling errors in GeoIP lookup

# Check if an IP address is provided
if len(argv) != 2:
    print("Usage: python ip_lookup.py <IP_ADDRESS>")
    exit(1)

ip_address = argv[1]

# === Load GeoIP Database ===
# Ensure the GeoIP database file is in the same directory as this script or provide the full
def load_geoip_database(db_path):
    try:
        return geoip2.database.Reader(db_path)
    except Exception as e:
        print(f"Error loading GeoIP database: {e}")
        exit(1)

# Example usage:
# reader = load_geoip_database('GeoLite2-City.mmdb')

# === Perform Lookup ===

def lookup_ip(reader, ip_address):
    try:
        response = reader.city(ip_address)
        print(f"IP Address: {ip_address}")
        print(f"Country: {response.country.name} ({response.country.iso_code})")
        print(f"Region: {response.subdivisions.most_specific.name} ({response.subdivisions.most_specific.iso_code})")
        print(f"City: {response.city.name}")
        print(f"Latitude: {response.location.latitude}, Longitude: {response.location.longitude}")
    except geoip2.errors.AddressNotFoundError:
        print(f"IP address {ip_address} not found in the database.")
    except Exception as e:
        print(f"Error looking up IP address: {e}")


# === Main Function ===
def main():
    db_path = 'GeoLite2-City.mmdb'  # Path to the GeoIP database file
    reader = load_geoip_database(db_path)
    lookup_ip(reader, ip_address)
    reader.close()

# === Run the script ===
if __name__ == "__main__":
    main()

