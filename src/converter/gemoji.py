import json
import sys

src_file_name = sys.argv[1]
raw_data = open(src_file_name, 'r').read()
data = json.loads(raw_data)

for stuff in data:
    if 'emoji' in stuff:
        emoji = stuff['emoji']
        aliases = stuff['aliases']
        tags = stuff['tags']

    if (len(aliases) > 0):
        for alias in aliases:
            print(emoji, alias, sep='\t')
    if (len(tags) > 0):
        for tag in tags:
            print(emoji, tag, sep='\t')
