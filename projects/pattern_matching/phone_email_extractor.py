# Get the text of clipboard
import pyperclip, re

text_to_search = pyperclip.paste()

# Phone regex
phone_regex = re.compile(r'''(
                                 (\d{3} | \(\d{3}\))?		 # Area code
                                 (\s|-|\.)?					 # Separator
                                 (\d{3})						 # First 3 digits
                                 (\s|-|\.)?  				 # Separator
                                 (\d{4})				         # Last 4 digits
                                 (\s*(ext|x|ext.)\s*(\d{2,5}))? # Extension
                        )''', re.VERBOSE)

# Email regex
email_regex = re.compile(r'''(
                                [a-zA-Z0-9._%+-]+ 	# username
                                @					# @ symbol
                                [a-zA-Z0-9.-]+ 		# domain name
                                (\.[a-zA-Z]{2,4})	# top level domain
                        )''', re.VERBOSE)
emails = email_regex.findall(text_to_search)

# Paste them onto the clipboard
matches = []
for groups in phone_regex.findall(text_to_search):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_number += ' x' + groups[8]
    matches.append(phone_number)

for groups in email_regex.findall(text_to_search):
    matches.append(groups[0])

# Copy result back to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
