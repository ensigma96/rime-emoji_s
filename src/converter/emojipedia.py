import xmltodict
import sys

src_file_name = sys.argv[1]
raw_data = open(src_file_name, 'r').read()
data = xmltodict.parse(raw_data, dict_constructor=dict)

for entry in data['d:dictionary']['d:entry']:
    emoji = ''
    name = ''
    if entry['@id'] != 'version':
        for index in entry['d:index']:
            if '@d:title' in index:
                emoji = index['@d:title']
                name = index['@d:value']
                name = name.replace(' ', '_')
                print(emoji, name, sep = '\t')
