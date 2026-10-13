def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a, b = matrix[0]
    c, d = matrix[1]
    det = a*d - b*c
    if det==0:
        return None
    a, d = d, a 
    b, c = -b, -c 
    a/=det
    b/=det
    c/=det
    d/=det 
    return [[a, b], [c, d]]