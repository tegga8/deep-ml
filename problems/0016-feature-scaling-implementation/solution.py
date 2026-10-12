
import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    m = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    mn = np.min(data, axis=0)
    mx = np.max(data, axis=0)

    standardized_data = np.divide(
        data - m, std,
        out=np.zeros_like(data, dtype=float),
        where=std != 0
    )

    normalized_data = np.divide(
        data - mn, mx - mn,
        out=np.zeros_like(data, dtype=float),
        where=(mx - mn) != 0
    )

    standardized_data = np.round(standardized_data, 4)
    normalized_data = np.round(normalized_data, 4)

    return standardized_data, normalized_data
