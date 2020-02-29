import numpy as np
import diversipy


def test_distance_to_boundary():
    points = np.array([[0.1, 0.2], [0.3, 0.9]])
    np.testing.assert_almost_equal(
        diversipy.distance.distance_to_boundary(points), np.array([0.1, 0.1])
    )
    np.testing.assert_almost_equal(
        diversipy.distance.distance_to_boundary(points, cuboid=((-1, -1), (2, 2))),
        np.array([1.1, 1.1]),
    )


def test_distance_matrix():
    points1 = np.array([[0.1, 0.2], [0.3, 0.9], [0.6, 0.1]])
    points2 = np.array([[0.2, 0.2]])
    # test L1 distance
    np.testing.assert_almost_equal(
        diversipy.distance.distance_matrix(points1, points2, norm=1),
        [[0.1], [0.1 + 0.7], [0.4 + 0.1]],
    )
    # test L2 distance
    np.testing.assert_almost_equal(
        diversipy.distance.distance_matrix(points1, points2, norm=2),
        [[0.1], [(0.1 ** 2 + 0.7 ** 2) ** 0.5], [(0.4 ** 2 + 0.1 ** 2) ** 0.5]],
    )
    # test toridal L1 distance
    np.testing.assert_almost_equal(
        diversipy.distance.distance_matrix(points1, points2, norm=1, max_dist=[1, 1]),
        [[0.1], [0.1 + (1 - 0.7)], [0.4 + 0.1]],
    )
