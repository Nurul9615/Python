#! python3
# bulletPointAdder.py - Adds wiki bullet points to start of each line of text in clipboard

import sys
import pyperclip

text = pyperclip.paste()

lines = text.split('\n') # A list
print(lines)

for i in range(len(lines)):
	lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

# pyperclip.copy(text)	

