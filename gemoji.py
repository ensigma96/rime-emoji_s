import json
import sys

src_file_name = sys.argv[1]
result_file_name = sys.argv[2]

raw_data = open(src_file_name, 'r').read()
# meta = open('src/dict/meta.yaml', 'r').read()
data = json.loads(raw_data)
result = open(result_file_name, 'a')

print('', file=result)

# print(type(data[0]))

for stuff in data:
  if 'emoji' in stuff:
    emoji = stuff['emoji']
    aliases = stuff['aliases']
    tags = stuff['tags']
    if (len(aliases) > 0):
      for alias in aliases:
        # use sep to replace spaces with tabs in output
        word_freq = 10
        print(emoji, alias, word_freq, sep='\t', file=result)
    if (len(tags) > 0):
      for tag in tags:
        word_freq = 10
        print(emoji, tag, word_freq, sep='\t', file=result)
