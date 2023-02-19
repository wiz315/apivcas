from tronpy import Tron

client = Tron()  
balance = client.get_account_balance(str('TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi'))
print (balance)