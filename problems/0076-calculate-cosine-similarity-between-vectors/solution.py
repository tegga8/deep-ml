import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	dot = np.dot(v2, v1)
	a = np.linalg.norm(v1, ord = 2)
	b = np.linalg.norm(v2, ord = 2)
	return dot/(a*b)