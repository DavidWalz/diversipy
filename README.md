# diversipy
[![Build Status](https://travis-ci.org/DavidWalz/diversipy.svg?branch=master)](https://travis-ci.org/DavidWalz/diversipy) [![Documentation Status](https://readthedocs.org/projects/diversipy/badge/?version=latest)](https://diversipy.readthedocs.io/en/latest/?badge=latest)

*This is a fork of [diversipy](https://pypi.org/project/diversipy/) in order to provide bug fixes and issue tracking.*

diversipy is a collection of algorithms dealing with three different but related topics. The first topic is super-uniform sampling of the unit hypercube. ‘Super-uniform’ in this context means that the obtained point sample should be more uniform than a random uniform sample, which is a desirable property in many applications. One such application is the design of computer experiments, where typically space-filling experimental designs are used. After creation, the samples can be transformed from the unit hypercube to arbitrary cuboids.

The task of subset selection is defined as follows: suppose you have a set of points in R^n and want to select a sample of them distributed as uniformly as possible. This may be necessary because the original set is too large to be processed entirely. The selection problem is related to clustering, with the difference that when using clustering, you usually want to retain the structure of the original point set.

Once one has created (or obtained from somewhere) a point set, one may want to assess its properties. Therefore, diversipy contains several functions to measure diversity and a few related concepts. Several different indicators are offered because they have different advantages and disadvantages (in terms of run time and what they measure).

#### Installation
```
pip install git+https://github.com/DavidWalz/diversipy.git
```

#### Example
```python
from diversipy import *
design = transform_spread_out(lhd_matrix(50, 2)) # create latin hypercube design
subset = psa_select(design, 10) # select subset, for whatever reason
unanchored_L2_discrepancy(subset) # calculate discrepancy
```
Note that points are stored row-wise, in accordance with numpy convention.
