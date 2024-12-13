# Python script to convert a file to hexadecimal
file_path = r"D:\geth\marksheet.pdf"

with open(file_path, "rb") as file:
    hex_data = file.read().hex()

print(hex_data)
