# Checks if passed number matches the pattern ddd-ddd-dddd
# d indicates digit


def is_valid_phone(text: str) -> True:
    if not len(text) == 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if not text[3] == '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if not text[7] == '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


print('Is 444-555-6666 a valid phone number : ' + str(is_valid_phone('444-555-6666')))
print('Is 444-555-666 a valid phone number : ' + str(is_valid_phone('444-555-666')))
print('Is 444-555-666e a valid phone number : ' + str(is_valid_phone('444-555-666e')))

statement = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(statement)):
    message = statement[i:i + 12]
    if is_valid_phone(message):
        print('Phone number found :' + message)
