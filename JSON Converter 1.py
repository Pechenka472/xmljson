import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
data_dict = []

for i in root[0].findall('item'):
    data_dict.append({'pubDate': i.find("pubDate").text, 'title': i.find('title').text})

with open('news1.json', 'wb') as json_file:
    file = json.dumps(data_dict, indent=4, ensure_ascii=False).encode('utf8')
    json_file.write(file)
