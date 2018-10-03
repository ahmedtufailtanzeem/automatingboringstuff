def word_count(statement):
	letter_count_dict = {}
	for letter in statement:
		letter_count_dict.setdefault(letter, 0)
		letter_count_dict[letter] += 1
	print(letter_count_dict)

statement = "The quick brown fox jumps over the lazy dog"
word_count(statement)

print("\n\n")
stock = {"Apples":5, "Strawberry":10, "Blue berry":2000, "Raspberry":100}
print(" Inventory ".center(12+5, "-"))
for k, v in stock.items():
	print(k.ljust(12, ".")+str(v).rjust(5))
