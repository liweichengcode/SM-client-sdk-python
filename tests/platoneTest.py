from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatONE
from hexbytes import HexBytes

# get blockNumber syncing gasPrice accounts evidences consensusStatus
# w3 = Web3(HTTPProvider("http://localhost:6789"))
w3=Web3(HTTPProvider(" http://58.251.94.108:56789"))  #含有国密链的节点
platone = PlatONE(w3)
block_number = platone.blockNumber
print(block_number)
print(platone.syncing)
print(platone.gasPrice)
print(platone.accounts)
print(platone.evidences)
print(platone.consensusStatus)

# get Balance
address = 'lax1yjjzvjph3tw4h2quw6mse25y492xy7fzwdtqja'
balance = platone.getBalance(address)
print(balance)
