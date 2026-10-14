import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x) = (h(x)*g'(x) - h'(x)*g(x)) / (h(x)^2) 
    """
    g = np.poly1d(g_coeffs)
    h = np.poly1d(h_coeffs)
    g_p = g.deriv()
    h_p = h.deriv()
    g_px = g_p(x)
    h_px = h_p(x)    
    gx = g(x)
    hx = h(x)
    if hx==0:
        raise ZeroDivisionError()
    num = (hx*g_px) - (h_px*gx)
    den = hx**2
    return float(num/den)