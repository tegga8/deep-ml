def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	ans = []
	for r in matrix:
		cur = []
		for ele in r:
			cur.append(ele*scalar)
		ans.append(cur)
	return  ans