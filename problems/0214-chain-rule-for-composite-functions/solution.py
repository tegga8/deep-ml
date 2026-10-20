import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	eval_map = {
		'square': lambda u: u**2,
		'sin': lambda u: np.sin(u),
		'exp': lambda u: np.exp(u),
		'log': lambda u: np.log(u)
	}
	
	deriv_map = {
		'square': lambda u: 2 * u,
		'sin': lambda u: np.cos(u),
		'exp': lambda u: np.exp(u),
		'log': lambda u: 1.0 / u
	}

	cur = x
	inter = []

	for i in reversed(functions):
		inter.append(cur)
		cur = eval_map[i](cur)
	
	d = 1

	for f, u in zip(functions, reversed(inter)):
          d *= deriv_map[f](u)
	
	return float(d)