
:mod:`hycusampling` --- Uniform sampling of the unit hypercube
==============================================================

.. automodule:: diversipy.hycusampling
    :synopsis: Uniform sampling of the unit hypercube.


Sampling algorithms
-------------------

Stratified sampling
~~~~~~~~~~~~~~~~~~~

.. autofunction:: stratify_conventional
.. autofunction:: stratify_generalized
.. autofunction:: stratified_sampling
.. autofunction:: reconstruct_strata_from_points


Latin hypercube designs
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: lhd_matrix
.. autofunction:: improved_lhd_matrix
.. autofunction:: has_lhd_property


Lattices
~~~~~~~~

.. autofunction:: rank1_design_matrix
.. autofunction:: korobov_design_matrix


Other
~~~~~

.. autofunction:: maximin_reconstruction
.. autofunction:: random_k_means
.. autofunction:: halton
.. autofunction:: random_uniform
.. autofunction:: grid
.. autofunction:: sukharev_grid


Helper functions
----------------

.. autofunction:: unitcube
.. autofunction:: scaled
.. autofunction:: transform_perturbed
.. autofunction:: transform_cell_centered
.. autofunction:: transform_spread_out
.. autofunction:: transform_anchored
.. autofunction:: shifted_randomly
