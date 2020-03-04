
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

Other
~~~~~

.. autofunction:: sample_halton
.. autofunction:: sample_maximin
.. autofunction:: sample_k_means
.. autofunction:: grid


Helper functions
----------------

.. autofunction:: unitcube
.. autofunction:: design_to_unitcube
.. autofunction:: is_latin
