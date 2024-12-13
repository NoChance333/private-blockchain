import json

# File paths
hex_file_path = r"D:\geth\marksheet.pdf"
json_file_path = r"D:\geth\marksheet_hex.json"

# Read the file and convert to hexadecimal
with open(hex_file_path, "rb") as file:
    hex_data = file.read().hex()

# Create a dictionary to store the data
data = {"hex": hex_data}

# Save to a JSON file
with open(json_file_path, "w") as json_file:
    json.dump(data, json_file)

print(f"Hexadecimal data saved to {json_file_path}")
