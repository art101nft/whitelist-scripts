import json

# Use this script to tally up addresses and amounts from N number of CSV files
# CSV files should consist of 2 items:
# address,amount
#
# execute the script and pipe the output to a new .json file


master_dict, output_dict = dict(), dict()
total_amount = 0

def read_file(name):
    with open(name, 'r') as f:
        details = f.readlines()
        for i in details:
            address = i.split(',')[0].lower()
            amount = int(i.split(',')[1].strip())
            if name == 'holders.csv':
                amount = amount + 1
            if address not in master_dict:
                master_dict[address] = 0

            master_dict[address] += amount

if __name__ == '__main__':
    read_file('nfs.csv')
    read_file('mnd.csv')
    read_file('bb.csv')
    for i in master_dict:
        total_amount += master_dict[i]
        output_dict[i] = str(master_dict[i])
    print(json.dumps(output_dict))
    # print(total_amount)
