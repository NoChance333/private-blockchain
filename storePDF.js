const Web3 = require('web3'); // Import the Web3 library
const web3 = new Web3('http://127.0.0.1:7545'); // Ganache local node

const contractABI = [
  {
    "inputs": [],
    "name": "hexData",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": true
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_hexData",
        "type": "string"
      }
    ],
    "name": "storeData",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getData",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": true
  }
];
const contractAddress = '0x4Ccd2a33b6b38c06BdE893153e64baCa42fe615A'; // Your contract address

const contract = new web3.eth.Contract(contractABI, contractAddress);

const hexData = "0x..."; // Replace with your actual PDF data in hex format

async function storePDF() {
  const accounts = await web3.eth.getAccounts();

  contract.methods.storeData(hexData).send({ from: accounts[0] })
    .on('transactionHash', (hash) => {
      console.log('Transaction hash:', hash);
    })
    .on('receipt', (receipt) => {
      console.log('Transaction was mined in block number:', receipt.blockNumber);
    });
}

storePDF();
