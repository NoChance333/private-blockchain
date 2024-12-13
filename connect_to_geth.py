from web3 import Web3

# Connect to your local Geth instance
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Check if the connection is successful
if w3.is_connected():
    print("Connected to Ethereum!")
else:
    print("Connection failed.")
