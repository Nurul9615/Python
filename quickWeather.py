#! python3

import json
import requests
import sys

# stringOfJsonData = '{"name": "Zophie", "isCat": true}'
# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)

if len(sys.argv) > 4:
	print('Usage: quickweather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])