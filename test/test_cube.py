import numpy as np
import diversipy


def test_unitcube():
    assert diversipy.cube.unitcube(dimension=2) == ([0, 0], [1, 1])


def test_grid():
    np.testing.assert_almost_equal(
        diversipy.cube.grid(n_levels=2, dimension=2),
        [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]],
    )
    np.testing.assert_almost_equal(
        diversipy.cube.grid(n_levels=2, dimension=2, sukharev=True),
        [[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]],
    )


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
    D = diversipy.cube.rank1_design(10, dimension=4)
    assert np.all(D >= 0) and np.all(D < 10)

    D = diversipy.cube.rank1_design(100, dimension=4, g=[4, 5, 7, 11])
    assert np.all(D >= 0) and np.all(D < 100)


def test_latin_design():
    X = diversipy.cube.latin_design(num_points=100, dimension=5)
    assert diversipy.cube.is_latin(X)


def test_improved_latin_design():
    X = diversipy.cube.improved_latin_design(num_points=100, dimension=5)
    assert diversipy.cube.is_latin(X)


def test_design_to_unitcube():
    D = diversipy.cube.latin_design(10, 5)
    X = diversipy.cube.design_to_unitcube(D, transform="centered")
    assert np.min(X) == 0.05
    assert np.max(X) == 0.95

    X = diversipy.cube.design_to_unitcube(D, transform="spread")
    assert np.min(X) == 0
    assert np.max(X) == 1

    X = diversipy.cube.design_to_unitcube(D, transform="perturbed")
    assert (X >= 0).all()
    assert (X <= 1).all()

    X = diversipy.cube.design_to_unitcube(D, transform="shifted")
    assert (X >= 0).all()
    assert (X <= 1).all()
