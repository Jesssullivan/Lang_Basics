
# prob.writeLP("scratch.lp")

prob.solve()

prob.
print(prob)


xs, ys = zip(*parse(condition).values())