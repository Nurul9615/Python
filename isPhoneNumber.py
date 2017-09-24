# Example phone number 332-524-1823
# Check for phone number expression
# Nurul Amin 22/09/17

import re # regex

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # r is a raw string so doesn't escape characters
Nurul = phoneNumRegex.search('My phone number is (932) 432-4823') # Returns a match object
print('First group is: ' + Nurul.group(1))
print('Second group is: ' + Nurul.group(2))
print('Phone number is: ' + Nurul.group())
areaCode, mainNumber = Nurul.groups()


def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

message = 'Call me at 415-555-1911 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: ' + chunk)
print('Done')	