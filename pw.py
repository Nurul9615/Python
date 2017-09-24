#! python3
# pw.py - insecure password locker program

import sys
import pyperclip

PASSWORDS = {'email': 'F879asdjasadi87safA',
	     'blog': 'Vkajsd8u2h76asdhlajd',
	     'luggage': '87232'}

if len(sys.argv) < 2:
	print('Usage: python pw.y [account] - copy account password' )
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)
		 
