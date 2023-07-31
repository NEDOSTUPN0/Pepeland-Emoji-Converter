import json
import os
import zipfile

zip_files = [f for f in os.listdir() if f.endswith('.zip')]

if len(zip_files) == 0:
    print('No zip files found')
elif len(zip_files) > 1:
    print('Warning: multiple zip files found, using the first one')

zip_file_name = zip_files[0]
zip_file_path = f'assets/minecraft/font/default.json'

with zipfile.ZipFile(zip_file_name, 'r') as z:
    with z.open(zip_file_path) as f:
        data = json.load(f)['providers']

output = []
seen = set()
for item in data:
    if item['file'].endswith('black.png') or 'z_iainternal:gui/' in item['file']:
        continue
    file_name = item['file'].split('/')[-1].split('.')[0]
    char = item['chars'][0]
    if file_name not in seen:
        output.append(f'"{file_name};{char}"')
        seen.add(file_name)
result = '[\n  ' + ',\n  '.join(output) + '\n]'

output_file_name = 'emojitype.json'
i = 1
while os.path.exists(output_file_name):
    output_file_name = f'emojitype{i}.json'
    i += 1

with open(output_file_name, 'w') as f:
    f.write(result)
