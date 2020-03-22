import requests
import pandas
import re

data = []

url = "https://en.wikipedia.org/wiki/Comparison_of_programming_languages"

response = requests.get(url)

langlist = re.compile(r'<th><a href=\"/[\w\s\/]*\"[\w\s]*=\"[\w\s]*\">([\w\s]*)<\/a>[\w\s]*<\/th>[\w\s]*<td>([\w\s]*)<\/td>')

languages = re.findall(langlist, response.text)

for l in languages:
	language = l[0]
	description = l[1]
	data.append((language, description))




