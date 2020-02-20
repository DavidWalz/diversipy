import numpy as np
import diversipy


def test_unitcube():
    assert diversipy.unitcube(dimension=2) == ([0, 0], [1, 1])


def test_scaled():
    points = np.array([[-10, -1], [10, 1]])
    np.testing.assert_almost_equal(
        diversipy.scaled(
            points=points,
            from_cuboid=([-10, -1], [10, 1]),
            to_cuboid=diversipy.unitcube(2),
        ),
        np.array([[0, 0], [1, 1]]),
    )


def test_grid():
    np.testing.assert_almost_equal(
        diversipy.grid(num_points=4, dimension=2),
        np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
    )


def test_sukharev_grid():
    np.testing.assert_almost_equal(
        diversipy.sukharev_grid(num_points=4, dimension=2),
        np.array([[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]]),
    )


def test_random_uniform():
    X = diversipy.random_uniform(num_points=100, dimension=20)
    assert (X >= 0).all() and (X <= 1).all() and X.shape == (100, 20)


def test_halton():
    X = diversipy.halton(num_points=100, dimension=20)
    assert (X >= 0).all() and (X <= 1).all() and X.shape == (100, 20)


def test_random_k_means():
    X = diversipy.random_k_means(num_points=100, dimension=20)
    assert (X >= 0).all() and (X <= 1).all() and X.shape == (100, 20)


def test_maximin_reconstruction():
    X = diversipy.maximin_reconstruction(num_points=100, dimension=5)
    assert (X >= 0).all() and (X <= 1).all() and X.shape == (100, 5)


def test_stratify_conventional():
    pass


def test_stratify_generalized():
    pass


def test_stratified_sampling():
    pass


def test_reconstruct_strata_from_points():
    pass


def test_rank1_design_matrix():
    pass


def test_korobov_design_matrix():
    pass


def test_lhd_matrix():
    X = diversipy.lhd_matrix(num_points=100, dimension=5)
    assert diversipy.has_lhd_property(X)


def test_improved_lhd_matrix():
    X = diversipy.improved_lhd_matrix(num_points=100, dimension=5)
    assert diversipy.has_lhd_property(X)


def test_transform_anchored():
    X = np.array([[0, 2], [1, 1], [2, 0]])
    np.testing.assert_almost_equal(
        diversipy.transform_anchored(X), [[0, 2 / 3], [1 / 3, 1 / 3], [2 / 3, 0]]
    )


def test_transform_perturbed():
    X = diversipy.lhd_matrix(100, 5)
    X = diversipy.transform_perturbed(X)
    assert (X >= 0).all() and (X <= 1).all()


def test_transform_cell_centered():
    X = np.array([[0, 2], [1, 1], [2, 0]])
    np.testing.assert_almost_equal(
        diversipy.transform_cell_centered(X),
        [[1 / 6, 5 / 6], [3 / 6, 3 / 6], [5 / 6, 1 / 6]],
    )


def test_transform_spread_out():
    X = np.array([[0, 2], [1, 1], [2, 0]])
    np.testing.assert_almost_equal(
        diversipy.transform_spread_out(X), [[0, 1], [0.5, 0.5], [1, 0]]
    )


def test_shifted_randomly():
    X = np.random.rand(100, 5)
    X = diversipy.shifted_randomly(X)
    assert (X >= 0).all() and (X <= 1).all()
