from bs4 import BeautifulSoup
import urllib.request
import csv

def write(indexString):
	# build url
	baseUrl = 'http://dwin-335-310-50-d1.language.berkeley.edu/radler/table.php?idx='
	url = baseUrl + indexString

	# build csv content
	result = [];

	# read the content from the url resource
	with urllib.request.urlopen(url) as response:
		html = response.read()

	# wrap the read html content to make it readable
	content = BeautifulSoup(html)

	# get the header word
	header = content.find_all('a')[0].string
	result.append(header)

	# get the translation of the word
	translation = content.find_all('span')[0].string
	result.append(translation)

	# get the tensed-word tags
	tensedWord = content.find_all('td')

	# future tags
	future = tensedWord[0:3] 
	future1 = tensedWord[4:9]
	for _f in future:
		result.append(_f.string)
	for _f1 in future1:
		result.append(_f1.string)

	# present tags
	present = tensedWord[9:13]
	for _p in present:
		result.append(_p.string)

	# past tags
	past = tensedWord[13:]
	for _past in past:
		result.append(_past.string)

	with open('test.csv', 'a') as fp:
		wr = csv.writer(fp, dialect = 'excel')
		wr.writerows([result])
	fp.close()

