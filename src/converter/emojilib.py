import json
import sys

src_file_name = sys.argv[1]
raw_data = open(src_file_name, 'r').read()
data = json.loads(raw_data)

fitzpatrick_scale_modifiers = ['🏻', '🏼', '🏽', '🏾', '🏿']
zwj = '\u200d'

def space2underscore(str):
    return str.replace(' ', '_')

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
                print(item, space2underscore(k), sep = '\t')
