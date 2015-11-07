from bs4 import BeautifulSoup
import urllib.request
from store import write

url = 'http://dwin-335-310-50-d1.language.berkeley.edu/radler/'

with urllib.request.urlopen(url) as response:
    html = response.read()

content = BeautifulSoup(html)

tags = content.find_all('a')[2:]

for _t in tags:
    index = _t['href'].replace('table.php?idx=', '')
    write(index)
