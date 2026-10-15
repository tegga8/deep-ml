import numpy as np


def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.

    :param A: Coefficient matrix (n x n)
    :param b: Right-hand side vector (n,)
    :return: Solution vector x (n,)
    """
    A = A.astype(float)
    b = b.astype(float)

    n = len(b)

    Ab = np.column_stack((A, b))

    for i in range(n):
        
        max_row = i + np.argmax(np.abs(Ab[i:n, i]))

        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]

        if np.isclose(Ab[i, i], 0.0):
            raise ValueError("Matrix is singular or nearly singular.")

        for k in range(i + 1, n):
            factor = Ab[k, i] / Ab[i, i]
            Ab[k, i:] -= factor * Ab[i, i:]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1 : n], x[i + 1 : n])) / Ab[i, i]

    return x
