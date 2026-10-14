import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	grad = np.array(gradient, dtype=float)
	mag = np.linalg.norm(grad, ord = 2)
	if mag==0.0:
		zero_dir = np.zeros_like(grad).tolist()
		return {
			"magnitude" : 0.0,
			"direction" : zero_dir, 
			"descent_direction": zero_dir
		}
	dr = grad/mag
	des_dr = -dr
	return {
			"magnitude" : mag,
			"direction" : dr, 
			"descent_direction": des_dr
		}