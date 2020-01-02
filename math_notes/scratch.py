import pulp as p

# initialize some PuLP variables:
prob = p.LpProblem('prob', p.LpMaximize)
x = p.LpVariable("x", lowBound=0)  # Create a variable x >=
y = p.LpVariable("y", lowBound=0)


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
goal = x + (2 * y)
inputs = [y <= 4 * x, y >= .25 * x, y <= 5 - x]

# run:
results = lpMax(goal, inputs, prob)
print(str('Results:\n' + str(results)))
