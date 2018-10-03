import re

test_to_search = '222-32-6715 526-94-7601 22-234 8888-88 222-32-2816'
ssn_regex = re.compile(r'\d{3}-\d{2}-\d{4}')
match_object = ssn_regex.sub('*', test_to_search)
print(match_object)