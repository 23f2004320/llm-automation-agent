import json
from pathlib import Path

# Define file paths
input_file = Path("C:/Users/visha/Music/TDS project-1/data/contacts.json")
output_file = Path("C:/Users/visha/Music/TDS project-1/data/contacts-sorted.json")

# Load contacts from JSON file
try:
    with open(input_file, "r", encoding="utf-8") as f:
        contacts = json.load(f)  # Load JSON array
except FileNotFoundError:
    print(f" Error: {input_file} not found.")
    exit(1)
except json.JSONDecodeError:
    print(f" Error: {input_file} is not a valid JSON file.")
    exit(1)

# Check if the file contains valid data
if not isinstance(contacts, list):
    print(f" Error: {input_file} does not contain a JSON array.")
    exit(1)

# Sort contacts by last_name, then by first_name
contacts_sorted = sorted(contacts, key=lambda c: (c["last_name"].lower(), c["first_name"].lower()))

# Save sorted contacts to output file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(contacts_sorted, f, indent=4)

print(f" Sorted contacts saved to {output_file}")
