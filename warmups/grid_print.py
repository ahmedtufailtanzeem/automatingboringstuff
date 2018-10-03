l = [
	['a1', 'b1', 'c1', 'd1'],
	['a2', 'b2', 'c2', 'd2'],
	['a3', 'b3', 'c3', 'd3'],
]

# Regular print
# for i in range(len(l)):
# 	for j in range(len(l[i])):
# 		print(l[i][j], end="")
# 	print()

# Column first print
for y in range(len(l[0])):
	for x in range(len(l)):
		print(l[x][y], end="")
	print()
