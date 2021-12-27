from xrsolver import V
from xrsolver import Problem

import solver

# This example is the third case from https://www.youtube.com/watch?v=WJEZh7GWHnw

s = solver.Solver()

x11 = V("x11", lb=0)
x12 = V("x12", lb=0)
x13 = V("x13", lb=0)
x21 = V("x21", lb=0)
x22 = V("x22", lb=0)
x23 = V("x23", lb=0)

p = Problem()
p.addVariable(x11)
p.addVariable(x12)
p.addVariable(x13)
p.addVariable(x21)
p.addVariable(x22)
p.addVariable(x23)

p.appendConstraint(x11 + x12 + x13 == 5000)
p.appendConstraint(x21 + x22 + x23 == 6000)
p.appendConstraint(x11 + x21 == 6000)
p.appendConstraint(x12 + x22 == 4000)
p.appendConstraint(x13 + x23 == 1000)

p.appendObjective(3 * x11 + 2 * x12 + 7 * x13 + 7 * x21 + 5 * x22 + 2 * x23)

s.solveProblem(p)
print("x11 =", x11.getValue())
print("x12 =", x12.getValue())
print("x13 =", x13.getValue())
print("x21 =", x21.getValue())
print("x22 =", x22.getValue())
print("x23 =", x23.getValue())

