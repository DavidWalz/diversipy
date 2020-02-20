import numpy as np
import diversipy


def test_psa_partition():
    pass


def test_psa_select():
    X = diversipy.grid(num_points=125, dimension=3)
    subset = diversipy.psa_select(points=X, num_selected_points=3)
    np.testing.assert_almost_equal(
        subset, [[0.0, 0.5, 0.5], [0.75, 0.0, 0.5], [0.75, 0.75, 0.5]],
    )


def test_select_greedy_maximin():
    X = diversipy.grid(num_points=125, dimension=3)
    subset = diversipy.select_greedy_maximin(
        points=X, num_selected_points=3, existing_points=X[0]
    )
    np.testing.assert_almost_equal(
        subset, [[1.0, 1.0, 1.0], [0.0, 0.5, 1.0], [0.5, 1.0, 0.0]]
    )


def test_select_greedy_maxisum():
    X = diversipy.grid(num_points=125, dimension=3)
    subset = diversipy.select_greedy_maxisum(
        points=X, num_selected_points=3, existing_points=X[0]
    )
    np.testing.assert_almost_equal(
        subset, [[1.0, 1.0, 1.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]]
    )


def test_select_greedy_energy():
    X = diversipy.grid(num_points=125, dimension=3)
    subset = diversipy.select_greedy_energy(
        points=X, num_selected_points=3, existing_points=X[0]
    )
    np.testing.assert_almost_equal(
        subset, [[1.0, 1.0, 1.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]]
    )