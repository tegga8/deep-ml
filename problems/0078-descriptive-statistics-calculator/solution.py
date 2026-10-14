import numpy as np
from scipy import stats

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    arr = np.asarray(data, dtype=float)
    if arr.size==0:
        raise ValueError
    mean = np.mean(data)
    med = np.median(arr)
    mode_res = stats.mode(arr, keepdims = True)
    mode_val = mode_res.mode[0]
    var_val = np.var(arr)
    std_val = np.std(arr)
    p25, p50, p75 = np.percentile(arr, [25, 50, 75])
    iqr = p75 - p25
    return {
        "mean": float(mean),
        "median": float(med),
        "mode": float(mode_val),
        "variance": float(var_val),
        "standard_deviation": float(std_val),
        '25th_percentile': p25, '50th_percentile': p50, '75th_percentile': p75, 'interquartile_range': iqr
    }