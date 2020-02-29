
:mod:`cube` --- Uniform sampling from the unit hypercube
==============================================================

.. automodule:: diversipy.cube
    :synopsis: Uniform sampling from the unit hypercube.


Sampling algorithms
-------------------

Stratified sampling
~~~~~~~~~~~~~~~~~~~

.. autofunction:: stratify_conventional
.. autofunction:: stratify_generalized
.. autofunction:: sample_from_strata
.. autofunction:: strata_from_points


Designs
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: latin_design
.. autofunction:: improved_latin_design
.. autofunction:: is_latin
.. autofunction:: rank1_design
.. autofunction:: korobov_design


Other
~~~~~

.. autofunction:: sample_halton
.. autofunction:: sample_maximin
.. autofunction:: sample_k_means
.. autofunction:: grid



Helper functions
----------------

.. autofunction:: unitcube
.. autofunction:: scaled
.. autofunction:: transform_perturbed
.. autofunction:: transform_cell_centered
.. autofunction:: transform_spread_out
.. autofunction:: transform_anchored
.. autofunction:: shifted_randomly
