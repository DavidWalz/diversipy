"""
diversipy is a collection of algorithms for (super-uniform) sampling in hypercubes and
polytopes, and for selecting diverse subsets and measuring diversity.

For further documentation see the submodules.
"""

from . import cube
from . import simplex
from . import polytope
from . import subset
from . import indicator
from . import distance

__all__ = ["cube", "simplex", "polytope", "subset", "indicator", "distance"]
__version__ = "0.9"
