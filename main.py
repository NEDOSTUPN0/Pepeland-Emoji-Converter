import json

with open('default.json', 'r') as f:
    data = json.load(f)['providers']

output = []
for item in data:
    if item['file'].endswith('black.png'):
        continue
    file_name = item['file'].split('/')[-1].split('.')[0]
    char = item['chars'][0]
    output.append(f'"{file_name};{char}"')
result = '[\n  ' + ',\n  '.join(output) + '\n]'

with open('emojitype.json', 'w') as f:
    f.write(result)