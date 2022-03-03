import json

# Use this script to tally up addresses and amounts and report
# on high level totals for the whitelist. How many addresses
# and how many tokens are whitelisted.

with open('output.json', 'r') as f:
    d = f.read()
    data = json.loads(d)
    amt = 0
    for i in data:
        amt += int(data[i])
    print(f'{len(data)} addresses with total of {amt} tokens available to mint in WL')
