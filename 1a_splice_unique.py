import json

# Use this script to tally up unique addresses and amounts from N number of CSV files
# CSV files should consist of 2 items:
# address,amount
#
# execute the script and pipe the output to a new .json file


master_dict, output_dict = dict(), dict()
all_addresses = list()
total_amount = 0

def read_file(name):
    master_dict[name] = dict()
    with open(name, 'r') as f:
        details = f.readlines()
        for i in details:
            address = i.split(',')[0].lower()
            amount = int(i.split(',')[1].strip())
            master_dict[name][address] = amount
            if address not in all_addresses:
                all_addresses.append(address)

if __name__ == '__main__':
    read_file('nfs.csv')
    read_file('mnd.csv')
    read_file('bb.csv')
    for address in all_addresses:
        amount = 0
        if address in master_dict['nfs.csv']:
            amount = master_dict['nfs.csv'][address]

        if address in master_dict['mnd.csv']:
            if master_dict['mnd.csv'][address] < amount:
                amount = master_dict['mnd.csv'][address]
        else:
            amount = 0

        if address in master_dict['bb.csv']:
            if master_dict['bb.csv'][address] < amount:
                amount = master_dict['bb.csv'][address]
        else:
            amount = 0

        if amount:
            output_dict[address] = str(amount)

    print(json.dumps(output_dict))
