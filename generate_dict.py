import json

raw_data = open('src/dict/emoji.json', 'r').read()
meta = open('src/dict/meta.yaml', 'r').read()
data = json.loads(raw_data)
result = open('dest/emoji_s.dict.yaml', 'w')
print(meta, '\n', sep='', file=result)

# print(type(data[0]))

for stuff in data:
  if 'emoji' in stuff:
    emoji = stuff['emoji']
    aliases = stuff['aliases']
    tags = stuff['tags']
    if (len(aliases) > 0):
      for alias in aliases:
        # use sep to replace spaces with tabs in output
        print(emoji, alias, sep='\t', file=result)
    if (len(tags) > 0):
      for tag in tags:
        print(emoji, tag, sep='\t', file=result)
