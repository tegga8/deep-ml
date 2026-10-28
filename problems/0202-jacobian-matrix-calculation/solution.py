import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
    x = np.array(x, dtype=float)
    n = len(x)
    m = len(f(x.tolist()))
    J = np.zeros((m, n))

    for j in range(n):
        x1 = x.copy()
        x2 = x.copy()
        x1[j] += h
        x2[j] -= h
        J[:, j] = (np.array(f(x1.tolist())) - np.array(f(x2.tolist()))) / (2 * h)

    return J.tolist()