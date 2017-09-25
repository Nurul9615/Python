import bs4
import requests

res = requests.get('http://nostarch.com')
res.raise_for_status()

# rest.text contains a string of all the HTML from the website
noStarchSoup = bs4.BeautifulSoup(res.text, "lxml")
# print(type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "lxml")
elems = exampleSoup.select('#author')
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
pElems[0].getText()
print(str(pElems[1]))
pElems[1].getText()
print(str(pElems[2]))
pElems[2].getText()

soup = bs4.BeautifulSoup(open('example.html'), "lxml")
spanElem = soup.select('span')[0]
spanElem.get('id')
print(spanElem.attrs)
print(spanElem.get('some_nonexistent_address') == None)