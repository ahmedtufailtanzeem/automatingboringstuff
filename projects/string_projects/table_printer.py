tableData = [
	['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose'],
]

# Fetch the number of columns
for column in range(len(tableData[0])):
	for row in range(len(tableData)):
		col_width = len(max(tableData[row], key=len))
		print(tableData[row][column].rjust(col_width), end=' ')
	print()

"""
l = ['apple', 'banana', 'strawberry', 'ugni']
# Prints ugni
print(max(l))

# Prints based on length
print(max(l, key=len))

# Prints based on length
print(len(max(l, key=len)))
"""