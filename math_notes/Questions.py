import numpy as np
from combos import *

"""
Problem:
A local pizza shop is offering a special deal on a "Surprise Pie," which comes with 3 different toppings,
but the pizza chef gets to choose the toppings.
The pizza shop offers 8 "usual" toppings, like sausage, bacon, pepperoni, peppers, onions, mushrooms, broccoli, and olives.
It also offers 5 "unusual" toppings, like anchovies, shrimp, reindeer, eggs, and potatoes.

What is the probability that the pizza has only "unusual" toppings?
60/1716 == (5/13)*(4/12)*(3/11) == (5*4) / (13*12*11)



What is the probability that the pizza has exactly 1 "usual" topping?
?
What is the probability that the pizza has exactly 2 "usual" toppings?
?
What is the probability that the pizza has exactly 3 "usual" toppings?
?
What is the probability that the pizza has at least one "usual" topping?
?
"""

"""
A steroid detection test is 97% effective at detecting steroid use, meaning that the probability of a user testing positive is 0.97. 
Unfortunately, it has a false positive rate of 5%, meaning the the probability of of a nonuser testing positive is 0.05.
A large university estimates that about 6% of its athletes use steroids. 
The universitys quarterback tests positive for steroids, yet he claims he does not use them. What are the chances that he is telling the truth?
?
Suppose that it rains in Spain an average of once every 13 days, and when it does, hurricanes have a 6% chance of happening in Hartford. 
When it does not rain in Spain, hurricanes have a 4% chance of happening in Hartford. What is the probability that it rains in Spain when hurricanes happen in Hartford? 
(Round your answer to four decimal places.)
?
"""
a,g,c




pxy = (0,0)
pval = init[pxy]
prow = init[pxy[0]]

for r in range(len(init)):
    print(init[r] + (prow * -(init[r][pxy[1]] / pval)))


import pulp as p
# initialize some PuLP variables:
prob = p.LpProblem('prob', p.LpMaximize)
x = p.LpVariable("x", lowBound=0)  # Create a variable x >=
y = p.LpVariable("y", lowBound=0)
z = p.LpVariable("z", lowBound=0)

def lpMax(goal, inputs, prob):
    prob += goal
    for equ in inputs:
        prob += equ
    prob.solve()
    results = {}
    # results['prob'] = prob
    for var in prob.variables():
        results[var] = var.varValue
    results['optimal'] = p.value(prob.objective)
    return results

# example values:
goal = x+y+z
inputs = [(7*x)+(6*y) <= 1135, (y*4)+ (z*8) <= 1060, (x*3)+(z*2) <= 455]

# run:
results = lpMax(goal, inputs, prob)
print(str('Results:\n' + str(results)))


from re import sub
def condition(x):

    if int(2*x[0]) - int(x[1]) >= 3:
        return True
    else:
        return False
set.


def parse(fx, i=0):
    feasible = dict()
    def handler(ln):
        return sub('[()\n]', '', ln).split(',')
    with open('io.txt') as io:
        for ln in io:
            if fx(handler(ln)):
                result = [int(i) for i in handler(ln)]
                feasible[i] = result
                i += 1
    return feasible

# run: #

print(parse(condition).values())
Optimal Solution: p = 45; -6     -1     -3 x = 5, y = 0, z = 5