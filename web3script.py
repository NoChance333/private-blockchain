from web3 import Web3

# Connect to your Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Check if connection is successful
if w3.isConnected():
    print("Connected to Ethereum!")

# Path to your keystore file
keystore_path = "D:/geth/data/keystore/UTC--2024-12-13T12-07-17.494767100Z--774f3e34c8f526f1f7d7641c89cd2813a8ed3e63"

# Load your account using the keystore file and password
with open(keystore_path) as f:
    keystore_data = f.read()

# Unlock the account
password = "123"  # Your account password
account = w3.eth.account.from_key(keystore_data, password)

# You can now use the account for transactions
print(f"Account address: {account.address}")
