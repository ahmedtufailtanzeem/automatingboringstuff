import re

text_to_replace = ''' This is a a wonderful place to  stay for many many  years!!'''
print(text_to_replace)

# Replace multiple spaces
text_to_replace = re.compile(r'(\s)\s').sub(r'\1', text_to_replace)

# Replace repeated words
text_to_replace = re.compile(r' (\w+) \1').sub(r' \1', text_to_replace)

# Replace multiple special symbols
text_to_replace = re.compile(r'([.!])[.!]').sub(r'\1', text_to_replace)
print(text_to_replace)
