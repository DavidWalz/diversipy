import diversipy
import numpy as np


def test_calc_dists_to_boundary():
    points = np.array([[0.1, 0.2], [0.3, 0.9]])
    np.testing.assert_almost_equal(
        diversipy.calc_dists_to_boundary(points), np.array([0.1, 0.1])
    )
    np.testing.assert_almost_equal(
        diversipy.calc_dists_to_boundary(points, cuboid=((-1, -1), (2, 2))),
        np.array([1.1, 1.1]),
    )


def test_calc_euclidean_dist_matrix():
    points1 = np.array([[0, 0], [0, 1], [1, 0]])
    points2 = np.array([[0.5, 0]])
    np.testing.assert_almost_equal(
        diversipy.calc_euclidean_dist_matrix(points1, points2),
        np.array([[0.5], [(0.5 ** 2 + 1) ** 0.5], [0.5]]),
    )


def test_calc_manhattan_dist_matrix():
    points1 = np.array([[0, 0], [0, 1], [1, 0]])
    points2 = np.array([[0.5, 0]])
    np.testing.assert_almost_equal(
        diversipy.calc_manhattan_dist_matrix(points1, points2),
        np.array([[0.5], [0.5 + 1], [0.5]]),
    )


def test_DistanceMatrixFunction():
    points1 = np.array([[0, 0], [0, 1], [1, 0]])
    points2 = np.array([[0.5, 0]])
    np.testing.assert_almost_equal(
        diversipy.DistanceMatrixFunction(exponent=1)(points1, points2),
        diversipy.calc_manhattan_dist_matrix(points1, points2),
    )
    np.testing.assert_almost_equal(
        diversipy.DistanceMatrixFunction(exponent=2)(points1, points2),
        diversipy.calc_euclidean_dist_matrix(points1, points2),
    )
    np.testing.assert_almost_equal(
        diversipy.DistanceMatrixFunction(exponent=np.inf)(points1, points2),
        np.array([[0.5], [1], [0.5]]),
    )
