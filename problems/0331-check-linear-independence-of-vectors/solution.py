import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    n = len(vectors)
    vectors = [row[:] for row in vectors]
    if n==0:
        return True
    m = len(vectors[0])
    c = 0
    rank = 0
    i = 0
    while i<n and c<m:
        cur = i 
        for j in range(i+1, n):
            if abs(vectors[j][c]) > abs(vectors[cur][c]):
                cur = j
        if abs(vectors[cur][c]) < 1e-6:
            c+=1
            continue
        if cur!=i:
            vectors[i], vectors[cur] = vectors[cur], vectors[i]

        for k in range(i+1, n):
            fact = vectors[k][c] / vectors[cur][c]
            for col in range(m):
                vectors[k][col]-=fact*vectors[cur][col]
        rank+=1
        c+=1
        i+=1 
    return rank==n