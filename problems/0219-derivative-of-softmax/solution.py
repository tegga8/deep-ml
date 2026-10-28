
from math import exp
import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
    s = []
    sum_exp = 0

    for ele in x:
        sum_exp += exp(ele)

    for ele in x:
        cur = exp(ele) / sum_exp
        s.append(cur)

    m = len(x)
    J = np.zeros((m, m))

    for i in range(m):
        for j in range(i, m):
            if i == j:
                J[i][j] = s[i] * (1 - s[i])
            else:
                J[i][j] = J[j][i] = -s[i] * s[j]

    return J.tolist()
