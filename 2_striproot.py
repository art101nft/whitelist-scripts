import json

from os import system

# Use this script to read a generated merkle proof file and remove the
# "root" item from the dict for preparation to publish to your website
#
#  assumes you've run "go-merkle-distributor --json-file=output.json"

with open('addr-to-claim.json', 'r') as f:
    file = f.read()

d = json.loads(file)

d.pop('root')

d = json.dumps(d)

print(d)
