import pytest
import numpy as np
import diversipy


def test_unitcube():
    assert diversipy.cube.unitcube(dimension=2) == ([0, 0], [1, 1])


def test_scaled():
    points = np.array([[-10, -1], [10, 1]])
    np.testing.assert_almost_equal(
        diversipy.cube.scaled(
            points=points,
            from_cuboid=([-10, -1], [10, 1]),
            to_cuboid=diversipy.cube.unitcube(2),
        ),
        [[0, 0], [1, 1]],
    )


def test_grid():
    np.testing.assert_almost_equal(
        diversipy.cube.grid(num_points=4, dimension=2),
        [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]],
    )
    diversipy.cube.grid(num_points=125, dimension=3)  # this should work
    with pytest.raises(AssertionError):
        diversipy.cube.grid(num_points=100, dimension=3)  # wrong number of points


def test_sukharev_grid():
    np.testing.assert_almost_equal(
        diversipy.cube.sukharev_grid(num_points=4, dimension=2),
        [[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]],
    )

    diversipy.cube.sukharev_grid(num_points=125, dimension=3)  # ok

    # wrong number of points
    with pytest.raises(AssertionError):
        diversipy.cube.sukharev_grid(num_points=100, dimension=3)


def test_sample_halton():
    X = diversipy.cube.sample_halton(num_points=100, dimension=20)
    assert (X >= 0).all() and (X <= 1).all() and X.shape == (100, 20)


def test_sample_k_means():
    X = diversipy.cube.sample_k_means(num_points=100, dimension=20)
    assert (X >= 0).all() and (X <= 1).all() and X.shape == (100, 20)


def test_sample_maximin():
    X = diversipy.cube.sample_maximin(num_points=100, dimension=5)
    assert (X >= 0).all() and (X <= 1).all() and X.shape == (100, 5)


def test_stratify_conventional():
    pass


def test_stratify_generalized():
    pass


def test_sample_from_strata():
    pass


def test_strata_from_points():
    pass


def test_rank1_design_matrix():
    pass


def test_korobov_design_matrix():
    pass


def test_latin_design():
    X = diversipy.cube.latin_design(num_points=100, dimension=5)
    assert diversipy.cube.is_latin(X)


def test_improved_latin_design():
    X = diversipy.cube.improved_latin_design(num_points=100, dimension=5)
    assert diversipy.cube.is_latin(X)


def test_transform_anchored():
    X = np.array([[0, 2], [1, 1], [2, 0]])
    np.testing.assert_almost_equal(
        diversipy.cube.transform_anchored(X), [[0, 2 / 3], [1 / 3, 1 / 3], [2 / 3, 0]]
    )


def test_transform_perturbed():
    X = diversipy.cube.latin_design(100, 5)
    X = diversipy.cube.transform_perturbed(X)
    assert (X >= 0).all() and (X <= 1).all()


def test_transform_cell_centered():
    X = np.array([[0, 2], [1, 1], [2, 0]])
    np.testing.assert_almost_equal(
        diversipy.cube.transform_cell_centered(X),
        [[1 / 6, 5 / 6], [3 / 6, 3 / 6], [5 / 6, 1 / 6]],
    )


def test_transform_spread_out():
    X = np.array([[0, 2], [1, 1], [2, 0]])
    np.testing.assert_almost_equal(
        diversipy.cube.transform_spread_out(X), [[0, 1], [0.5, 0.5], [1, 0]]
    )


def test_shifted_randomly():
    X = np.random.rand(100, 5)
    X = diversipy.cube.shifted_randomly(X)
    assert (X >= 0).all() and (X <= 1).all()
