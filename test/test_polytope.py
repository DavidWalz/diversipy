from diversipy import polytope
import numpy as np
import pytest


def test_constraints_from_bounds():
    A, b = polytope.constraints_from_bounds(lower=[1, 2], upper=[5, 6])
    np.testing.assert_almost_equal(A, [[-1, 0], [0, -1], [1, 0], [0, 1]])
    np.testing.assert_almost_equal(b, [-1, -2, 5, 6])


def test_check_constraints():
    polytope.check_Ab(A=np.ones((2, 3)), b=np.ones(2))  # ok

    with pytest.raises(Exception):
        polytope.check_Ab(A=np.ones((2, 3, 1)), b=np.ones(2))  # A must be 2-dimensional

    with pytest.raises(Exception):
        polytope.check_Ab(A=np.ones((2, 3)), b=np.ones(2, 2))  # b must be 1-dimensional

    with pytest.raises(Exception):
        polytope.check_Ab(
            A=np.ones((4, 3)), b=np.ones(2)
        )  # A and b must have same number of columns


def test_chebyshev_center():
    A, b = polytope.constraints_from_bounds(lower=[0, 0, 0], upper=[1, 1, 1])
    x0 = polytope.chebyshev_center(A, b)
    assert np.allclose(x0, [0.5, 0.5, 0.5])


def test_solve_equality():
    # x1 + x2 + x3 = 2
    A = np.array([[1, 1, 1]])
    b = np.array([2])
    N, xp = polytope.solve_equality(A, b)
    Z = np.random.uniform(low=-1, high=1, size=(5, 2))
    X = Z @ N.T + xp
    assert np.allclose(X @ A.T, b)


def test_hitandrun():
    pass  # tested in test_sample()


def test_sample():
    # Sampling from unit-simplex in R^3
    # 0 <= xi <= 1
    A1, b1 = polytope.constraints_from_bounds(lower=[0, 0, 0], upper=[1, 1, 1])
    # sum xi = 1
    A2 = np.array([[1, 1, 1]])
    b2 = np.array([1])
    X = polytope.sample(A=A1, b=b1, A_eq=A2, b_eq=b2, n_samples=1000)
    assert np.all(X @ A1.T <= b1)
    assert np.allclose(X @ A2.T, b2)

    # Sampling from R^2
    A = np.array([[-1, 0], [0, -1], [1, 0], [0, 1], [1 / 2, 1], [2 / 3, -1]])
    b = np.array([-0.1, -0.2, 0.7, 0.9, 1, -0.2])
    X = polytope.sample(A=A, b=b, n_samples=1000)
    assert np.all(X @ A.T <= b)
