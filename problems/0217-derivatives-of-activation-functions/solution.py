from math import exp
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	def sigmoid(x):
		return 1/(1 + exp(-x))
	def tanh(x):
		return (exp(x) - exp(-x))/(exp(x) + exp(-x))
	ans = {}
	ans['sigmoid'] = sigmoid(x)*(1 - sigmoid(x))
	ans['tanh'] = 1 - tanh(x)**2
	if x>0:
		ans['relu'] = 1
	else:
		ans['relu'] = 0
	return ans