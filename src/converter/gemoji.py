import json
import sys

src_file_name = sys.argv[1]

with open(src_file_name, 'r') as f:
    data = json.load(f)

for stuff in data:
    if 'emoji' in stuff:
        emoji = stuff['emoji']
        aliases = stuff['aliases']
        tags = stuff['tags']

        for alias in aliases:
            print(emoji, alias, sep='\t')

        for tag in tags:
            print(emoji, tag, sep='\t')
