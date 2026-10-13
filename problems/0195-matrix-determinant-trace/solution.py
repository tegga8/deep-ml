def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    n = len(matrix)
    if n == 0:
        return 0.0, 0.0
    trace_val = sum(matrix[i][i] for i in range(n))
    A = [row[:] for row in matrix]
    det_val = 1.0
    
    for i in range(n):
        pivot_row = i
        for r in range(i + 1, n):
            if abs(A[r][i]) > abs(A[pivot_row][i]):
                pivot_row = r
                
        if abs(A[pivot_row][i]) < 1e-12:
            return 0.0, trace_val

        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]
            det_val *= -1.0
            
        det_val *= A[i][i]
        
        for r in range(i + 1, n):
            factor = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= factor * A[i][c]
                
    return det_val, trace_val
