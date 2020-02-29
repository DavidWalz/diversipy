"""
diversipy is a collection of algorithms for sampling in hypercubes,
selecting diverse subsets, and measuring diversity.

For further documentation see the submodules.
"""

from . import cube
from . import simplex
from . import polytope
from . import subset
from . import indicator
from . import distance

__all__ = ["cube", "subset", "indicator", "distance"]
__version__ = "0.9"
