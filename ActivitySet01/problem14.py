# Using Web Services
# https://www.py4e.com/lessons/servces

import urllib.request

import xml.etree.ElementTree as ET

url = input('Enter URL: ')

if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_1416937.xml'

print(f"Retrieving {url}")


data = urllib.request.urlopen(url).read().decode()

print(f"Retrived {len(data)} characters")

tree = ET.fromstring(data)

counts = tree.findall('.//count')

print(f"Count: {len(counts)}")

count_list = list()

for item in counts:

    num = int(item.text)

    count_list.append(num)

print(f"Sum: {sum(count_list)}")

