import numpy as np
from scipy.linalg import lu as lu

"""

return np.dot(np.linalg.pinv(P-U), D)
"""

def tMX(A,D):
    # (I - A-1) * B = X:
    return np.dot(np.linalg.inv(np.identity(len(A)) - A), D)

A = np.array([[.1, .2], [.4, .5]])
D = np.array([[24000], [14000]])

print(tMX(A,D))
##def techMX(mx, D):
# (I - A-1) * B = X:
P, L, U = lu(A)
print(P)
print(L)
print(U)
print(I)
invmx = np.linalg.pinv(A)
np.matmul(I-invmx, D)

np.
prodX = techMX(A, D)


print(str('production vector X = : \n' + str(prodX)))
