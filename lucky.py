#! python3
# Search on google and open top results in new tabs

import requests
import sys
import webbrowser
import bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results
soup = bs4.BeautifulSoup(res.text)

# Open browser tab for each result, the elements all have class 'r'
linkElems = soup.select('.r a')
print(linkElems)

# open 5 search results or however many results you got back
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))