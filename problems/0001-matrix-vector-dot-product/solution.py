def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	l = len(a)
	ans = [0] * l
	la = len(a[0])
	
	lb = len(b)
	if la!=lb:
		return -1
	for i in range(l):
		
		for j in range(la):
			ans[i] += a[i][j]*b[j]
	return ans