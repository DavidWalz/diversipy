import numpy as np
from scipy.special import comb


def sample(dimension, n_points=1):
    """Draw samples from the unit simplex.

    Parameters
    ----------
    dimension : int
        number of variables.
    n_points : int, optional
        number of points to sample, by default 1

    Returns
    -------
    numpy array
        Random samples from the unit simplex
    """
    s = np.random.standard_exponential((n_points, dimension))
    return (s.T / s.sum(axis=1)).T


def grid(dimension, levels):
    """Construct a regular grid on the unit simplex.

    Parameters
    ----------
    dimension : int
        Number of variables.
    levels : int
        Number of levels between 0 and 1 for each variable.

    Returns
    -------
    ndarray of shape (n_points, n_dim)
        Regularily spaced grid points on the unit simplex.

    References
    ----------
    Nijenhuis and Wilf, Combinatorial Algorithms, Chapter 5, Academic Press, 1978.

    Examples
    --------
    >>> simplex.grid(3, 3)
    array([
        [0. , 0. , 1. ],
        [0. , 0.5, 0.5],
        [0. , 1. , 0. ],
        [0.5, 0. , 0.5],
        [0.5, 0.5, 0. ],
        [1. , 0. , 0. ]
    ])
    """
    m = dimension
    n = levels - 1
    n_points = comb(n + m - 1, m - 1, exact=True)

    x = np.zeros(m, dtype=int)
    x[-1] = n

    out = np.empty((n_points, m), dtype=int)
    out[0] = x

    h = m
    for i in range(1, n_points):
        h -= 1

        val = x[h]
        x[h] = 0
        x[h - 1] += 1
        x[-1] = val - 1

        if val != 1:
            h = m

        out[i] = x

    return out / n
