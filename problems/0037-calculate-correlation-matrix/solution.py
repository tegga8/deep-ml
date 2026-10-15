import numpy as np


def _as_2d(a, name):
    """Convert input to a float 2D array of shape (n_samples, n_features)."""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        a = a.reshape(-1, 1)
    elif a.ndim != 2:
        raise ValueError(f"{name} must be 1D or 2D, got {a.ndim}D.")
    return a


def calculate_correlation_matrix(X, Y=None, cross_only=True):
    """Calculate the Pearson correlation coefficient matrix.

    Columns are treated as variables and rows as observations.

    Constant columns (zero variance) have undefined correlation. Their
    off-diagonal entries are set to 0.0 and their diagonal entry to 1.0.

    :param X: array of shape (n_samples, n_features_X) or (n_samples,)
    :param Y: optional array of shape (n_samples, n_features_Y) or (n_samples,)
    :param cross_only: only used when Y is given. If True (default), return
        the (n_features_X, n_features_Y) block of correlations between X and
        Y columns. If False, return the full matrix over the columns of X
        followed by the columns of Y.
    :return: 2D numpy array of correlation coefficients
    :raises ValueError: on mismatched row counts, fewer than 2 samples,
        or non-finite values in the input
    """
    X = _as_2d(X, "X")

    if Y is not None:
        Y = _as_2d(Y, "Y")
        if X.shape[0] != Y.shape[0]:
            raise ValueError("X and Y must have the same number of rows.")
        data = np.column_stack((X, Y))
    else:
        data = X

    n_samples = data.shape[0]
    if n_samples < 2:
        raise ValueError("At least 2 samples are required.")
    if not np.isfinite(data).all():
        raise ValueError("Input contains NaN or infinite values.")

    centered = data - data.mean(axis=0)
    cov = centered.T @ centered / (n_samples - 1)
    std = np.sqrt(np.diag(cov))
    std_outer = np.outer(std, std)

    corr = np.zeros_like(cov)
    np.divide(cov, std_outer, out=corr, where=std_outer > 0)
    np.fill_diagonal(corr, 1.0)
    np.clip(corr, -1.0, 1.0, out=corr)

    if Y is not None and cross_only:
        return corr[: X.shape[1], X.shape[1]:]
    return corr