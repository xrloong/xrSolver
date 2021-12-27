from xrsolver.core.symbol import V
from xrsolver.core.problem import Problem

import solver

# This example is the first case from https://www.youtube.com/watch?v=WJEZh7GWHnw

s = solver.Solver()

x = V("x", lb=0)
y = V("y", lb=0)

p = Problem()
p.addVariable(x)
p.addVariable(y)

p.appendConstraint(0.25 * x + 0.50 * y <= 120)
p.appendConstraint(0.50 * x + 0.50 * y <= 150)
p.appendConstraint(0.25 * x <= 50)

p.appendObjective(12 * x + 15 *y)

s.solveProblem(p)
print("x =", x.getValue())
print("y =", y.getValue())

