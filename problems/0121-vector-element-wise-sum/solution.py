def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float] | int:

    c = []
    m, n = len(a), len(b)
    
    if m != n:
        return -1
        
    for i in range(m):
        c.append(a[i] + b[i])
        
    return c
