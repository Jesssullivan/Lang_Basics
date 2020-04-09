#!/usr/bin/env python3
# vanilla_ingredients = 1 * cream + 3 * vanilla + 1 * sugar
# chocolate_incredients = 4 * cream + 1 * vanilla + 1 * sugar
#
# v is number of quarts of vanilla
# c is number of quarts of chocolate
#
# profit = (5.50 * v) + (3.25 * c)
#
# constraints:
#   cream:   v + (4 * c) <= 1440
#   vanilla: (3 * v) + c <=  855
#   sugar:   v + c <= 405
from sympy import Symbol, symbols
from sympy.solvers import solve

a,c,g = symbols('a c g')
soln1 = solve([ + 4*c - 1440, 3*v + c - 1135])  #, v + c - 405]
c1 = soln1[c]
v1 = soln1[v]

soln2 = solve([3*v + c - 855, v + c - 405])
c2 = soln2[c]
v2 = soln2[v]

soln3 = solve([v + 4*c - 1440, v + c - 405])
c3 = soln3[c]
v3 = soln3[v]

def profit(c, v): return (5.5 * v) + (3.25 * c)

print("intersections(c,v) = \t{}, \t{}, \t{}".format((c1,v1), (c2,v2), (c3,v3)))
print("profit(c,v)        = \t{}, \t{}, \t{}".format(profit(c1, v1), profit(c2, v2), profit(c3, v3)))