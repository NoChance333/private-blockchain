pragma solidity ^0.8.0;

contract StoreHexData {

    event PDFStored(string hexData, uint256 blockNumber);

    function storePDF(string memory hexData) public {
        
        emit PDFStored(hexData, block.number);
    }
}
