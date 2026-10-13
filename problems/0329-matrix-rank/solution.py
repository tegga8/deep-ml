import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    M = A.astype(float).copy()
    m, n = M.shape
    rank = 0
    c = 0
    
    for i in range(m):
        if c >= n:
            break
            
        pivot = i 
        for r in range(i + 1, m):
            if abs(M[pivot][c]) < abs(M[r][c]):
                pivot = r 
                
        if pivot != i:
            M[[i, pivot]] = M[[pivot, i]]
            
        if abs(M[i, c]) <= tol:
            c += 1
            continue
            
        for ind in range(i + 1, m):
            fact = M[ind, c] / M[i, c]
            M[ind, c:] -= fact * M[i, c:]
            
        rank += 1
        c += 1
        
    return rank
