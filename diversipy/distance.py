"""
This module provides distance measures. For more exotic distance functions have a look
at :mod:`scipy.spatial.distance`.
"""

import numpy as np
import diversipy


def distance_to_boundary(points, cuboid=None):
    """Calculate the distance of each point to the boundary of some cuboid.

    This distance is simply the minimum of all differences between
    a point and the lower and upper bounds. This function also checks if all
    calculated distances are larger than zero. If not, some points must be
    located outside the cuboid.

    Parameters
    ----------
    points : array_like
        2-D array of `n` points.
    cuboid : tuple of array_like, optional
        Contains the min and max bounds of the considered cuboid. If
        omitted, the unit hypercube is assumed.

    Returns
    -------
    distances : numpy array
        1-D array of `n` distances
    """
    if cuboid is None:
        cuboid = diversipy.cube.unitcube(points.shape[1])
    min_bounds, max_bounds = cuboid
    dists_to_min_bounds = (points - np.asarray(min_bounds)).min(axis=1)
    dists_to_max_bounds = (np.asarray(max_bounds) - points).min(axis=1)
    distances = np.minimum(dists_to_min_bounds, dists_to_max_bounds)
    assert np.all(distances >= 0.0)  # are all points contained in cuboid?
    return distances


def distance_matrix(points1, points2, norm=2, max_dist=None):
    """Calculate the distance between each combination of points in two sets.

    Parameters
    ----------
    points1 : array_like
        2-D array of `n1` points.
    points2 : array_like
        2-D array of `n2` points.
    norm : int, optional
        Norm to use for the distance, by default 2 (euclidean norm).
    max_dist : array_like, optional
        1-D array of largest possible distance in each dimension.
        Providing these values has the consequence of treating the cuboid as a torus.
        This is useful for eliminating edge effects induced by the lack of neighbor
        points outside the bounds of the cuboid.d

    Returns
    -------
    distances : numpy array
        (`n1` x `n2`) array of distances
    """
    points1 = np.atleast_2d(points1)
    points2 = np.atleast_2d(points2)
    assert points1.shape[1] == points2.shape[1]
    diff = np.expand_dims(points1, 1) - np.expand_dims(points2, 0)
    if max_dist is not None:
        diff = np.abs(diff)
        diff = np.minimum(diff, max_dist - diff)
        assert (diff >= 0).all()  # are all points inside the cuboid?
    return np.linalg.norm(diff, axis=-1, ord=norm)
