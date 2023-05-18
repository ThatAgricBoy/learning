#!/usr/bin/python3

""" Paste text from the clipboard
    Do something to it
    Copy the new text to the clipboard"""

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
