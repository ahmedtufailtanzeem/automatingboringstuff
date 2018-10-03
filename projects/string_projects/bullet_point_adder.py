import pyperclip

# Add's a *  to a new line separated list
# Sample text
'''
Lists of animals
Lists of amphibians by region
Lists of birds by region
Lists of cats
'''

# Copy text from clipboard
text = pyperclip.paste()
print(text)

# Append '* ' in front of each list item
lines = text.split('\n')
for index in range(len(lines)):
	lines[index] = '* ' + lines[index]
text = '\n'.join(lines)

# Copy back to clipboard
pyperclip.copy(text)
print(text)
