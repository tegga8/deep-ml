import numpy as np

def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v_m = np.linalg.norm(v, ord = 2)
	L_m = np.linalg.norm(L, ord = 2)
	L_hat = L/L_m
	return (np.dot(v, L)/L_m)*L_hat
