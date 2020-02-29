import numpy as np
import diversipy


def test_sample():
    X = diversipy.simplex.sample(dimension=3, n_points=1000)
    # points sum up to 1
    assert np.allclose(X.sum(axis=1), 1)
    # points are bounded in each dimension by 0 <= x_i <= 1
    assert np.min(X) >= 0
    assert np.min(X) <= 1


def test_grid():
    G = diversipy.simplex.grid(dimension=3, levels=5)
    # grid points are 3-vectors
    assert G.shape[1] == 3
    # all point need to sum up to 1
    assert np.allclose(G.sum(axis=1), 1)
    # all grid points are unique
    assert len(np.unique(G, axis=0)) == len(G)
    # in each dimension we have 4 levels (and 0)
    for i in range(3):
        assert np.allclose(np.unique(G[:, i]), [0, 0.25, 0.5, 0.75, 1])
