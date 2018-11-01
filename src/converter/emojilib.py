import json
import sys

src_file_name = sys.argv[1]

fitzpatrick_scale_modifiers = ['🏻', '🏼', '🏽', '🏾', '🏿']
zwj = '\u200d'

with open(src_file_name, 'r') as f:
    data = json.load(f)

for key in data:
    v = data[key]

    char = v['char']
    emojis = set([char])
    if v['fitzpatrick_scale']:
        for modifier in fitzpatrick_scale_modifiers:
            emojis.add(char + zwj + modifier)

    names = set([key] + v['keywords'])
    names_nospaces = set([])
    for item in names:
        names_nospaces.add(item.replace(' ', '_'))

    for emoji in sorted(emojis):
        for name in sorted(names_nospaces):
            print(emoji, name, sep='\t')
