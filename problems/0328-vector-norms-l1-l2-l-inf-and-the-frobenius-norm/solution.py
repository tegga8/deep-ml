import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # 1. Enforce strict 2D check for Frobenius norm
    if norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError("Frobenius norm is only defined for 2D matrices.")
        return float(np.linalg.norm(arr, ord='fro'))
    
    # 2. Handle entry-wise norms ('l1', 'l2', 'linf') safely across 1D and 2D arrays
    # Flattening ensures NumPy treats 2D matrices as a flat list of entries
    flat_arr = arr.ravel() 
    
    if norm_type == 'l1':
        return float(np.linalg.norm(flat_arr, ord=1))
    elif norm_type == 'l2':
        return float(np.linalg.norm(flat_arr, ord=2))
    elif norm_type == 'linf':
        return float(np.linalg.norm(flat_arr, ord=np.inf))
    else:
        raise ValueError(f"Unknown norm type: {norm_type}")
