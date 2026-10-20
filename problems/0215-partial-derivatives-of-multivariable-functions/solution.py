import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	if func_name == 'poly2d':
		x, y = point
		df_dx = 2 * x * y + y**2
		df_dy = x**2 + 2 * x * y
		return (float(df_dx), float(df_dy))
		
	elif func_name == 'exp_sum':
		x, y = point
		val = np.exp(x + y)
		return (float(val), float(val))
		
	elif func_name == 'product_sin':
		x, y = point
		df_dx = np.sin(y)
		df_dy = x * np.cos(y)
		return (float(df_dx), float(df_dy))
		
	elif func_name == 'poly3d':
		x, y, z = point
		df_dx = 2 * x * y
		df_dy = x**2 + z**2
		df_dz = 2 * y * z
		return (float(df_dx), float(df_dy), float(df_dz))
		
	elif func_name == 'squared_error':
		x, y = point
		df_dx = 2 * (x - y)
		df_dy = -2 * (x - y)
		return (float(df_dx), float(df_dy))
		
	else:
		raise ValueError(f"Unknown function name: {func_name}")
