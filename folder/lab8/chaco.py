#!/usr/bin/python3

import json

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

out = []
for i in data[:5]:
	name = i.get('name', 'N/A')
	html_url = i.get('html_url', 'N/A')
	updated_at = i.get('updated_at', 'N/A')
	visibility = i.get('visibility', 'N/A')

	line = f"{name},{html_url},{updated_at},{visibility}"
	out.append(line)

outfile = 'chacon.csv'
with open(outfile, 'w') as csv_file:
	csv_file.write("\n".join(out))
