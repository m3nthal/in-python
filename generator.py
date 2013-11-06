import numpy as np
import pylab as P

from scipy.stats import beta
rv = beta(8, 3)

x = np.linspace(0, np.minimum(rv.dist.b, 3))
h = P.plot(x, rv.pdf(x))

#P.show()

R = beta.rvs(3, 8)
print(R)
