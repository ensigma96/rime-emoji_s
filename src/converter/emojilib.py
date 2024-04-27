import json
import sys

src_file_name = sys.argv[1]

fitzpatrick_scale_modifiers = ['🏻', '🏼', '🏽', '🏾', '🏿']
zwj = '\u200d'

with open(src_file_name, 'r') as f:
    data = json.load(f)

for key in data:
    emoji = key

    for name in sorted(data[key]):
        print(emoji, name, sep='\t')
