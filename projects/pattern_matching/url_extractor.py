import re, pyperclip

# Copy text from clipboard
# text_to_search = pyperclip.paste()
text_to_search = 'http://www.google.com https://www.facebook.com https://www.amazon.in'

# Build regex object
url_regex = re.compile(r'http[s]?://\w{3}\.\w+\.\w{2,3}')
print(url_regex.findall(text_to_search))