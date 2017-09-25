#! python3

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))

resTwo = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
	# Always call raise for status
	resTwo.raise_for_status()
except Exception as exc:
	print("There was a problem: %s" % (exc))

# Check if request for web page succeeded, code in HTTP protocol for ok is 400
res.status_code == requests.codes.ok

playFile = open('RandJ.txt', 'wb')

# Create chunk on each iteration with 100000 bytes each
for chunk in res.iter_content(100000):
	playFile.write(chunk)

playFile.close()

print(res.text[:250])
