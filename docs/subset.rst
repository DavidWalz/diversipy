
:mod:`subset` --- Select diverse subsets
========================================

.. automodule:: diversipy.subset
    :synopsis: Select diverse subsets.


Part-and-select algorithm
-------------------------

.. autoclass:: MinBoundingBox
    :members:
.. autofunction:: psa_partition
.. autofunction:: psa_select


Greedy algorithms
-----------------

The algorithms in this group all follow the same pattern: they start with an
empty set and add one point per iteration. The selected point is the one with
the best assessment with regard to the already selected points, hence the
classification as greedy methods. The first point is chosen with regard to
the existing points. If no existing points are given, one of the candidate
points is randomly selected to act as an existing point. So, to enforce a
deterministic behavior, provide at least one existing point. The run time is
:math:`\Theta(n(N+E)M)` for n dimensions, M candidates, E existing, and
N selected points.

.. autofunction:: select_greedy_maximin
.. autofunction:: select_greedy_maxisum
.. autofunction:: select_greedy_energy