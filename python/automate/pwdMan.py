#!/usr/bin/python3
# pwdMan - An insecure password locker program

PASSWORDS = {'email': 'Ftjfnasdrhfjkdshjdf',
	     'blog': 'sdhfvnkbnbvjssfsfd',
	     'luggage': '124535'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pwdMan {account} - copy account password')
	sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)
