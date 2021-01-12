from client_sdk_python.packages.platone_account import Account

account = Account().create(net_type='lax', mode='SM')

print(account.address)

print(account.privateKey)
