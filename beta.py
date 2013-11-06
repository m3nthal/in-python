import numpy as np
import pylab as P
from scipy.stats import beta

rv1 = beta(3, 8)
x1 = np.linspace(0, np.minimum(rv1.dist.b, 3))
h = P.plot(x, rv1.pdf(x1))
rv2 = beta(8, 3)
x2 = np.linspace(0, np.minimum(rv2.dist.b, 3))
h = P.plot(x, rv2.pdf(x2))