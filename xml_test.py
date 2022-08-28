import urllib.request
import xml.etree.ElementTree as ET



url = input('Enter location: ')

total_comments = 0
sum_all = 0

print('Retrieving', url)
xml_file = urllib.request.urlopen(url).read()
print('Retrieved', len(xml_file), 'characters')

tree = ET.fromstring(xml_file)
counts = tree.findall('.//count')

for count in counts:
    sum_all += int(count.text)
    total_comments += 1

print('Count', total_comments)
print('Sum', sum_all)

# ******** output ********
# Enter location: http://python-data.dr-chuck.net/comments_42.xml
# Retrieving http://python-data.dr-chuck.net/comments_42.xml
# Retrieved 4189 characters
# Count 50
# Sum 2553