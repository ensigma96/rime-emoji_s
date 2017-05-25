import xmltodict
import sys

src_file_name = sys.argv[1]
result_file_name = sys.argv[2]

raw_data = open(src_file_name, 'r').read()
data = xmltodict.parse(raw_data, dict_constructor=dict)
result = open(result_file_name, 'a')

temp = []

curr_emoji = ''
for entry in data['d:dictionary']['d:entry']:
  if entry['@id'] != 'version':
    for index in entry['d:index']:
      # print(index)
      # print(type(index))
      if '@d:value' in index:
        if not ('@d:title' in index):
          curr_emoji = index['@d:value']
        else:
          name = index['@d:value']

          if (len(curr_emoji) <= 2):
            word_freq = 10
          else:
            word_freq = 5

          if ' ' in name:
            name = name.replace(' ', '_')
            word_freq = 1

          temp.append({'emoji': curr_emoji,  'name': name, 'word_freq': word_freq})
    curr_emoji = ''

print('', file=result)
for item in temp:
  print(item['emoji'], item['name'], item['word_freq'], sep='\t', file=result)