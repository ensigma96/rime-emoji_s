import json
import sys

src_file_name = sys.argv[1]

fitzpatrick_scale_modifiers = ['🏻', '🏼', '🏽', '🏾', '🏿']
zwj = '\u200d'

with open(src_file_name, 'r') as f:
    data = json.load(f)

for key in data:
    info = data[key]
    keywords = info['keywords']
    char = info['char']
    fitzpatrick_scale = info['fitzpatrick_scale']
    char_collection = set()
    keyword_collection = set()
    if char:
        char_collection.add(char)
        if fitzpatrick_scale:
            for modifier in fitzpatrick_scale_modifiers:
                char_collection.add(char + zwj + modifier)
        keyword_collection.add(key)
        keyword_collection.update(keywords)
        for item in sorted(char_collection):
            for k in sorted(keyword_collection):
                print(item, k.replace(' ', '_'), sep='\t')
