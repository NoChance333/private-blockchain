from web3 import Web3
from solcx import compile_source

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Ensure connection is successful
assert w3.is_connected

# Set your account and unlock it (make sure your account is unlocked in Geth or set up correctly)
account = '0x3897d2437183aceb8f898bf782fb255e6153dbf2'
private_key = 'your_private_key'  # Make sure to keep your private key secure

# Define the contract ABI and address
contract_address = '0xYourContractAddress'
contract_abi = [
    {
        "constant": False,
        "inputs": [{"name": "value", "type": "string"}],
        "name": "addData",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "index", "type": "uint256"}],
        "name": "getData",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Get the contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Create the transaction
nonce = w3.eth.getTransactionCount(account)
gas_price = w3.eth.gasPrice

# Set up the data to be added
data = "Hello, this is my custom data in block 93!"

# Build the transaction
tx = contract.functions.addData(data).buildTransaction({
    'chainId': 1,  # Mainnet; use 3 for Ropsten or your custom network ID
    'gas': 2000000,
    'gasPrice': gas_price,
    'nonce': nonce,
})

# Sign the transaction
signed_tx = w3.eth.account.signTransaction(tx, private_key)

# Send the transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

# Wait for the transaction to be mined
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(f"Transaction successful with hash: {tx_hash.hex()}")
