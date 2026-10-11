def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    m = len(a)
    n = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = a[j][i]
    return ans
