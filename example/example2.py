from xrsolver import V
from xrsolver import Problem

import solver

# This example is the second case from https://www.youtube.com/watch?v=WJEZh7GWHnw

s = solver.Solver()

x1 = V("x1", lb=0, ub=3)
x2 = V("x2", lb=0, ub=3)
x3 = V("x3", lb=0, ub=3)
x4 = V("x4", lb=0, ub=3)
x5 = V("x5", lb=0, ub=3)

p = Problem()
p.addVariable(x1)
p.addVariable(x2)
p.addVariable(x3)
p.addVariable(x4)
p.addVariable(x5)

p.appendConstraint(x1 + x2 <= 5)
p.appendConstraint(x2 <= 0.5 * (x1 + x2))
p.appendConstraint(x5 >= 0.4 * (x3 + x4))
p.appendConstraint(x1 + x2 + x3 + x4 +x5 == 10)

p.appendObjective(8.1 * x1 + 10.5 * x2 + 6.4 * x3 + 7.5 * x4 + 5.0 * x5)

s.solveProblem(p)
print("x1 =", x1.getValue())
print("x2 =", x2.getValue())
print("x3 =", x3.getValue())
print("x4 =", x4.getValue())
print("x5 =", x5.getValue())

