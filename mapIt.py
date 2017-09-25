#! python3
# mapIt.py - Launch maps in browser using the string in clipboard or CL

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
	# Join returns a single string value, better since CL arguments may have spaces between them
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)