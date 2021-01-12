from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatONE
from client_sdk_python.packages.platone_keys.utils import bech32,address
from hexbytes import HexBytes
from client_sdk_python.packages.eth_utils import to_checksum_address
true = True
false = False
# get blockNumber
# w3 = Web3(HTTPProvider("http://10.1.1.2:6789"))
# platon = PlatON(w3)
# w3 = Web3(HTTPProvider("http://10.1.1.5:6789"))
w3=Web3(HTTPProvider(" http://58.251.94.108:56789"))  #含有国密链的节点
platone = PlatONE(w3)
print(w3.isConnected())
from_address = "lax1yjjzvjph3tw4h2quw6mse25y492xy7fzwdtqja"
send_privatekey = "b7a7372e78160f71a1a75e03c4aa72705806a05cf14ef39c87fdee93d108588c"
block_number = platone.blockNumber
print(block_number)
print(platone.protocolVersion)
print(platone.accounts)
print(platone.syncing)
print(platone.gasPrice)
print(platone.evidences)
print(platone.consensusStatus)
platone.filter('latest')
print(platone.defaultBlock)
print("111")

# get Balance
from_address = 'lax1yjjzvjph3tw4h2quw6mse25y492xy7fzwdtqja'
# address = '0x493301712671Ada506ba6Ca7891F436D29185821'
balance = platone.getBalance(from_address)
print(balance)
platone.getPrepareQC(block_number)
platone.getStorageAt()
platone.getCode()
platone.getBlock()
platone.getBlockTransactionCount()
platone.getTransaction()
platone.getRawTransaction()
platone.getTransactionFromBlock()
platone.getTransactionByBlock()
platone.waitForTransactionReceipt()
platone.getTransactionReceipt()
platone.getTransactionCount()
platone.replaceTransaction()
platone.modifyTransaction()
platone.sendTransaction()
platone.sendRawTransaction()
platone.sign()
platone.call()
platone.estimateGas()
platone.filter()
platone.getFilterChanges()
platone.getFilterLogs()
platone.getLogs()
platone.uninstallFilter()
platone.generateGasPrice()
platone.setGasPriceStrategy()
platone.analyzeReceiptByHash()
platone.analyzeReceipt()
platone.ecrecover()

# sendtransaction
to_address = 'lax1qqqjkfwu854vf3ze2dpy5gctmxy3gdgzsngj66'
## Address = bech32.bech32_decode(from_address)
# hrpgot, data = bech32.decode("lax", from_address)
# from_address = to_checksum_address(bytes(data)).lower()
# # arguments = tuple(address.split(","))
# hrpgot, data = bech32.decode("lax", to_address)
# to_address = to_checksum_address(bytes(data)).lower()

w3.personal.unlockAccount(from_address, "123456", 999999)
data={
    "from": from_address,
    "to": to_address,
    "value": 1,
    "gas": 1000000,
    "gasPrice": 1000000000,
}
# provider = RPC connection http://10.1.1.2:6789
transaction_hex = HexBytes(platone.sendTransaction(data)).hex()
# b'{"jsonrpc":"2.0","id":2,"error":{"code":-32602,"message":"invalid argument 0: json: cannot unmarshal decoding bech32 failed: failed converting data to bytes: invalid character not part of charset: 98 into Go struct field CallArgs.from of type common.Address"}}\n'
result = platone.waitForTransactionReceipt(transaction_hex)
print(result)