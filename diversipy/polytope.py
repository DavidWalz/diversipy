"""This module provides functions to uniformly sample in the presence of linear inequality
constraints, :math:`Ax <= b`. This corresponds to sampling from a convex polytope.
Additional linear equality constraints :math:`Ax = b` are also supported.
"""
import numpy as np
import scipy.linalg
import scipy.optimize
from tqdm import tqdm


def check_Ab(A, b):
    """Check if matrix equation Ax=b is well defined.

    Parameters
    ----------
    A : ndarray of shape (n_constraints, n_dimensions)
        Left-hand-side of Ax <= b.
    b : ndarray of shape (n_constraints)
        Right-hand-side Ax <= b.
    """
    assert A.ndim == 2
    assert b.ndim == 1
    assert A.shape[0] == b.shape[0]


def chebyshev_center(A, b):
    """Find the center of the polytope.

    Parameters
    ----------
    A : ndarray of shape (n_constraints, n_dimensions)
        Left-hand-side of Ax <= b.
    b : ndarray of shape (n_constraints)
        Right-hand-side Ax <= b.

    Returns
    -------
    ndarray of shape (n_dimensions)
        Chebyshev center of the polytope
    """
    res = scipy.optimize.linprog(
        np.r_[np.zeros(A.shape[1]), -1],
        A_ub=np.hstack([A, np.linalg.norm(A, axis=1, keepdims=True)]),
        b_ub=b,
        bounds=(None, None),
    )
    if not res.success:
        raise Exception("Unable to find Chebyshev center")
    return res.x[:-1]


def constraints_from_bounds(lower, upper):
    """Construct the inequality constraints Ax <= b that correspond to the given
    lower and upper bounds.

    Parameters
    ----------
    lower : array-like
        lower bound of each dimension
    upper : [type]
        upper bound of each dimension

    Returns
    -------
    (A, b)
        A: ndarray of shape (2*n_dimensions, n_dimensions)
        b: ndarray of shape (2*n_dimensions)
    """
    n = len(lower)
    A = np.row_stack([-np.eye(n), np.eye(n)])
    b = np.r_[-np.array(lower), np.array(upper)]
    return A, b


def solve_equality(A, b):
    """Compute a basis for the nullspace of A, and a particular solution to A x = b.

    Parameters
    ----------
    A : ndarray of shape (n_constraints, n_dimensions)
        Left-hand-side of Ax <= b.
    b : ndarray of shape (n_constraints)
        Right-hand-side Ax <= b.

    Returns
    -------
    (N, xp)
        [description]
    """
    N = scipy.linalg.null_space(A)
    xp = np.linalg.pinv(A) @ b
    return N, xp


def hitandrun(A, b, x0):
    """Generator for the hit & run MCMC method sample from convex polytopes."""
    check_Ab(A, b)
    assert A.shape[1] == len(x0)

    x = x0

    while True:
        # sample random direction from unit hypersphere
        direction = np.random.randn(A.shape[1])
        direction /= np.linalg.norm(direction)

        # distances to each face from the current point in the sampled direction
        D = (b - x @ A.T) / (direction @ A.T)

        # distance to the closest face in and opposite to
        lo = np.max(D[D < 0])
        hi = np.min(D[D > 0])

        # make random step
        x += np.random.uniform(lo, hi) * direction
        yield x


def sample(A, b, n_samples=100, thin=1, A_eq=None, b_eq=None):
    """Sample a number of points from a convex polytope.

    Parameters
    ----------
    A : ndarray of shape (n_constraints, n_dimensions)
        Left-hand-side of Ax <= b.
    b : ndarray of shape (n_constraints)
        Right-hand-side Ax <= b.
    n_samples : int, optional
        Number of samples to generate, by default 100
    thin : int, optional
        The thinning factor of the generated samples. A thinning of 10 means a samples
        is taken every 10 steps.
    A_eq : ndarray of shape (n_constraints, n_dimensions)
        Left-hand-side of A_eq x = b_eq.
    b_eq : ndarray of shape (n_constraints)
        Right-hand-side A_eq x = b_eq.

    Returns
    -------
    [type]
        [description]
    """
    if (A_eq is not None) and (b_eq is not None):
        check_Ab(A_eq, b_eq)
        N, xp = solve_equality(A_eq, b_eq)
    else:
        N = np.eye(A.shape[1])
        xp = np.zeros(A.shape[1])

    # project to the subspace of solutions of the equality constraints
    At = A @ N
    bt = b - A @ xp

    x0 = chebyshev_center(At, bt)
    sampler = hitandrun(At, bt, x0)

    X = np.empty((n_samples, At.shape[1]))
    for i in tqdm(range(n_samples)):
        for _ in range(thin - 1):
            next(sampler)
        X[i] = next(sampler)

    # project back
    X = X @ N.T + xp
    return X
