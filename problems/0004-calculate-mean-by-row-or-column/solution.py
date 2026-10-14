import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    """
    Calculate the mean of a matrix along rows or columns.
    
    Args:
        matrix: A 2D list of floats.
        mode: Calculation direction ('row' or 'column').
        
    Returns:
        A list of floats representing the means.
    """

    matrix_arr = np.array(matrix, dtype=float)
    if mode == 'row':
        means = np.mean(matrix_arr, axis=1)
    elif mode == 'column':
        means = np.mean(matrix_arr, axis=0)
    else:
        raise ValueError("Mode must be either 'row' or 'column'")
    return means.tolist()
