#! python3
# downloadXkcd.py - download all comics on this page automatically

#The URL of the comic’s image file is given by the href attribute of an <img> element.
#The <img> element is inside a <div id="comic"> element.
#The Prev button has a rel HTML attribute with the value prev.
#The first comic’s Prev button links to the http://xkcd.com/\#

import requests
import bs4
import os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True) # Store comics in ./xkcd

while not url.endswith('#'):
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, "lxml")

	# Find url of comic image
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		try:
			# Download image
			comicURL = 'http:' + comicElem[0].get('src')
			print('Downloading image %s...' % (comicURL))
			res = requests.get(comicURL)
			res.raise_for_status()
		except requests.exceptions.MissingScheme: 
			# Skip comic (No comic on this page)
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + prevLink.get('href')
			continue

		# Save image to folder
		# os.path.basename returns the last part of the url like 'example.png'
		imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

		# Get prev buttons url
		prevLink = soup.select('a[rel="prev"]')[0]
		url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')