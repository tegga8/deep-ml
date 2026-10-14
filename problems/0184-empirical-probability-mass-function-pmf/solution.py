def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    samples = sorted(samples)
    d = {}
    tot = 0
    for ele in samples:
        d[ele] = d.get(ele, 0) + 1
        tot+=1
    ans = []
    for ele, cnt in d.items():
        ans.append((ele, float(cnt/tot)))
    return  ans