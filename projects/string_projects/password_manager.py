#!
# This project helps you in managing your passwords, insure though
# Reads a command line input(account name) and copies to clip board the matching account password

import sys
import pyperclip

# dictionary to store all passwords
PASSWORDS = {
	'email': 'emailGHG_$%jkJkjkg124',
	'blog': 'blogQAGHGHbjasbdj1234LKOI#',
	'luggage': 'luGG123#457',
}

# If no account is password exit the program after showing the Usage information
if len(sys.argv) < 2:
	print("Usage : py.py [account] - copy account password")
	sys.exit()
account = sys.argv[1]

# Check if account exist in PASSWORD dictionary
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS.get(account))
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)



