# Regex are patterns to match in a given input

# \d - Match a digit
# \d\d\d-\d\d\d-\d\d\d\d - Pattern to match a phone number
# \d{3}-\d{3}-\d{4} - Pattern to match a phone number but a little more complex

# import the re module to work with regex
# To get a Regex object re.compile(r'\d{3}-\d{3}-\d{4}')
# On Regex object invoke search method and it returns None if no match or Match object
# Use group() method to return actual match

# Import re module
import re

# Create Regex object matching your pattern, r indicates raw string
phone_match_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

# Pass the search string to Regex object search method
match_object = phone_match_regex.search('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')

# Get the match using the group method, group takes int value. 0 or empty means return the entire match text
print(match_object.group())

# Perform grouping using ()
# Remember (), *, ?, \ have special meaning so if you need to use \ them escape it

phone_match_regex = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')
match_object = phone_match_regex.search('Call me at (415)-555-1011 tomorrow. 415-555-9999 is my office.')
print(match_object.group(0))
# Area code
print(match_object.group(1))

# Mid code
print(match_object.group(2))

# Actual phone number code
print(match_object.group(3))

# Get a tuple of all group values
print(match_object.groups())  # --> ('415', '555', '9999')

# Matching multiple groups using |

hero_regex = re.compile(r'batman|hulk')
match_object = hero_regex.search('I love hulk and batman')
print(match_object.group())
match_object = hero_regex.search('I love batman and hulk')
print(match_object.group())

# Sub group matching
hero_regex = re.compile(r'bat(man|women|superman|catwomen)')
match_object = hero_regex.search('I love batsuperman')
print(match_object.group())
print(match_object.group(1))

# Optional mapping zero or 1 using ?
hero_regex = re.compile(r'bat(wo)?man')
match_object = hero_regex.search('I love batman')
print(match_object.group())

match_object = hero_regex.search('I love batwoman')
print(match_object.group())

# Zero or more using *
hero_regex = re.compile(r'bat(wo)*man')
match_object = hero_regex.search('I love batwowowoman')
print(match_object.group())

match_object = hero_regex.search('I love batman')
print(match_object.group())

# 1 or more +
hero_regex = re.compile(r'bat(wo)+man')
match_object = hero_regex.search('I love batwowowoman')
print(match_object.group())

# 'NoneType' object has no attribute 'group'
# match_object = hero_regex.search('I love batman')
# print(match_object.group())


# Matching specific repetition, like exactly 3 times etc
# They "{}" great reduce the regex \d\d\d\d\d --> \d{5} Can also specify upper and
# lower bound {3,5}, {3,}, {,5}(Match zero or 5)
# Python’s regular expressions are greedy by default, which means that in ambiguous situations
# they will match the longest string possible. Use ? to make them non-greedy
hero_regex = re.compile(r'(ha){1,5}')  # This is greedy by default and will give hahahahaha
match_object = hero_regex.search('I love to say hahahahahaha')
print(match_object.group())

# Greedy and Non-Greedy
hero_regex = re.compile(r'ha{1,5}?')  # Make it non-greedy
match_object = hero_regex.search('I love to say hahahahahaha')
print(match_object.group())

# findall method, this will return list of matching strings or tuple of string if used with groups
# [('415', '555', '9999'), ('212', '555', '0000')]
# ['415-555-9999', '212-555-0000'] If no groups specified
phone_num_regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
match_object = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(match_object)

# Character Classes predefined. We can make our own [0-5], [a-zA-Z0-9],[aeiouAEIOU]
# \d Any numeric digit from 0 to 9. \D Negation of \d
# \w Any letter, numeric digit, or the underscore character \W Negation of \w
# \s Any space, tab, or newline character \S Any character that is not a space, tab, or newline
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, hats'))

# Making your own character classes
# Use when you want to match a set of characters but Character classes are too broad Ex:aeiou
regex = re.compile(r'[aeiou]')
match_object = regex.findall('an apple a day, keeps doctor away')
print(match_object)

match_object = regex.search('an apple a day, keeps doctor away')
print(match_object.group())

# [a-zA-Z0-9]
# Remember inside the square bracketsnormal regular expressions are not interpreted. [a-z?]
# No special meaning for ? we are saying match a-e or ?
# No need to use escape sequence
regex = re.compile(r'[a-e?]')
match_object = regex.findall('an apple a? day, keeps doctor away')
print(match_object)

# ^ placing a caret character just after opening [] negates
regex = re.compile(r'[^aeiou]')
match_object = regex.findall('an apple a? day, keeps doctor away')
print(match_object)

# The caret and dollar Sign characters
regex = re.compile(r'^[I]')
match_object = regex.findall('I was amazingly wonderful guy at 23')
print(match_object)

regex = re.compile(r'\d$')
match_object = regex.findall('I was amazingly wonderful guy at 23')
print(match_object)

regex = re.compile(r'^\d+$')
match_object = regex.findall('I was amazingly wonderful guy at 23')
print(match_object)

# The wildcard character
# . match anything except new line
# \. to escape .
atRegex = re.compile(r'.at')
match_object = atRegex.findall('cat hat mat rat flat')
print(match_object)

# Match anything and everything
atRegex = re.compile(r'(First Name:.*)(Last Name:.+)')
match_object = atRegex.search('First Name: Tanzeem Last Name:Ahmed')
print(match_object.group(1))
print(match_object.group(2))

# Above is greedy by default use ? to make it non-greedy and match the shortest
atRegex = re.compile(r'First Name: <.+?>')
match_object = atRegex.search('First Name: <Tanzeem> Last Name:<Ahmed>')
print(match_object.group())

# Matching Newlines with the Dot Character
atRegex = re.compile(r'.*', re.DOTALL)
match_object = atRegex.search('First Name: Tanzeem \n Last Name:Ahmed')
print(match_object.group())

# Case-insensitive matching
atRegex = re.compile(r'batman', re.I)
match_object = atRegex.search('BATMAN')
print(match_object.group())

# Substituting String with the sub() Method
atRegex = re.compile(r'Agent \w+')
print(atRegex.sub('***** ', 'Agent Alice is our secret spy'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# Writing a verbose regex
phone_regex = re.compile(r'''(
	(\d{3} | \(\d{3}\))?		 # Area code
	(\s|-|\.)?					 # Separator
	\d{3}						 # First 3 digits
	(\s|-|\.)?  				 # Separator
	\d{4}				         # Last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})? # Extension
)''', re.VERBOSE)
# print(phone_regex.search('this is a phone number 111-222.3333').group())
# print(phone_regex.search('this is a phone number (111)-222.3333 extn 124').group())
# print(phone_regex.search('this is a phone number (111)-222.3333 extn 124').groups())
print(phone_regex.search('this is a phone number (111)-222.3333').groups())

# Combining re.DOTALL | re.IGNORECASE | re.VERBOSE using | Pipe and pass to second argument to compile