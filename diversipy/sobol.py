import numpy as np
from io import StringIO

DIM_MAX = 40  # maximum number of dimensions
LOG_MAX = 30  # maximum number of bits
POLY = np.genfromtxt(
    StringIO(
        """# POLY, and first 8 columns of V
        1, 1,  0,  0,  0,  0,  0,  0,  0
        3, 1,  0,  0,  0,  0,  0,  0,  0
        7, 1,  1,  0,  0,  0,  0,  0,  0
        11, 1,  3,  7,  0,  0,  0,  0,  0
        13, 1,  1,  5,  0,  0,  0,  0,  0
        19, 1,  3,  1,  1,  0,  0,  0,  0
        25, 1,  1,  3,  7,  0,  0,  0,  0
        37, 1,  3,  3,  9,  9,  0,  0,  0
        59, 1,  3,  7, 13,  3,  0,  0,  0
        47, 1,  1,  5, 11, 27,  0,  0,  0
        61, 1,  3,  5,  1, 15,  0,  0,  0
        55, 1,  1,  7,  3, 29,  0,  0,  0
        41, 1,  3,  7,  7, 21,  0,  0,  0
        67, 1,  1,  1,  9, 23, 37,  0,  0
        97, 1,  3,  3,  5, 19, 33,  0,  0
        91, 1,  1,  3, 13, 11,  7,  0,  0
        109, 1,  1,  7, 13, 25,  5,  0,  0
        103, 1,  3,  5, 11,  7, 11,  0,  0
        115, 1,  1,  1,  3, 13, 39,  0,  0
        131, 1,  3,  1, 15, 17, 63, 13,  0
        193, 1,  1,  5,  5,  1, 27, 33,  0
        137, 1,  3,  3,  3, 25, 17,115,  0
        145, 1,  1,  3, 15, 29, 15, 41,  0
        143, 1,  3,  1,  7,  3, 23, 79,  0
        241, 1,  3,  7,  9, 31, 29, 17,  0
        157, 1,  1,  5, 13, 11,  3, 29,  0
        185, 1,  3,  1,  9,  5, 21,119,  0
        167, 1,  1,  3,  1, 23, 13, 75,  0
        229, 1,  3,  3, 11, 27, 31, 73,  0
        171, 1,  1,  7,  7, 19, 25,105,  0
        213, 1,  3,  5,  5, 21,  9,  7,  0
        191, 1,  1,  1, 15,  5, 49, 59,  0
        253, 1,  1,  1,  1,  1, 33, 65,  0
        203, 1,  3,  5, 15, 17, 19, 21,  0
        211, 1,  1,  7, 11, 13, 29,  3,  0
        239, 1,  3,  7,  5,  7, 11,113,  0
        247, 1,  1,  5,  3, 15, 19, 61,  0
        285, 1,  3,  1,  1,  9, 27, 89,  7
        369, 1,  1,  3,  7, 31, 15, 45, 23
        299, 1,  3,  3,  9,  9, 25,107, 39
        """
    ),
    delimiter=",",
    dtype=int,
)


def _bit_lo0(n):
    """Position of the lowest 0-bit in the binary representation of integer `n`."""
    s = np.binary_repr(n)
    i = s[::-1].find("0")
    if i == -1:
        i = len(s)
    return i


def _init(n_dim):
    """Initialize the Sobol matrix"""
    poly = POLY[:, 0]
    V = np.zeros((DIM_MAX, LOG_MAX), dtype=int)
    V[:, :8] = POLY[:, 1:]

    # Set up remaining components of V, see Bratley and Fox, section 2.
    V[0] = 1
    for i in range(1, n_dim):
        # largest m where 2^m < poly[i]
        m = len(np.binary_repr(poly[i])) - 1
        # bit pattern for the given number excluding the leading 1
        include = np.array([int(b) for b in np.binary_repr(poly[i])[1:]])
        for j in range(m, LOG_MAX):
            V[i, j] = V[i, j - m]
            for k in range(m):
                if include[k]:
                    V[i, j] = np.bitwise_xor(V[i, j], 2 ** (k + 1) * V[i, j - k - 1])
    V *= 2 ** np.arange(LOG_MAX)[::-1]
    return V[:n_dim]


def _sobol(n_dim):
    """Generator for Sobol points"""
    V = _init(n_dim)
    lastq = np.zeros(n_dim, dtype=int)

    for i in range(2 ** LOG_MAX):
        sample = lastq / 2 ** LOG_MAX
        col = _bit_lo0(i)
        lastq = np.bitwise_xor(lastq, V[:, col])
        yield sample


def sample(n_dim, n_points=1, skip=1):
    """Generate a Sobol point set.

    Parameters
    ----------
    n_dim : int
        Number of dimensions
    n_points : int, optional
        Number of points to sample, by default 1
    skip : int, optional
        Number of points in the sequence to skip, by default 1

    Returns
    -------
    array, shape=(n_samples, n_dim)
        Samples from the Sobol sequence.
    """
    if not (1 <= n_dim <= DIM_MAX):
        raise ValueError("Sobol: n_dim must be between 1 and 40.")
    if n_points + skip >= 2**LOG_MAX:
        raise ValueError(f"Sobol: n_points must be < 2**{LOG_MAX} including skip")

    generator = _sobol(n_dim)
    for i in range(skip):
        next(generator)
    points = np.full((n_points, n_dim), np.nan)
    for i in range(n_points):
        points[i] = next(generator)
    return points
