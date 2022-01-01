from xrsolver import Problem

from xrsolver.solver.z3 import Solver

# This example is the first case from https://www.youtube.com/watch?v=WJEZh7GWHnw

s = Solver()

p = Problem()

x = p.generateVariable("x", lb=0)
y = p.generateVariable("y", lb=0)

p.addVariable(x)
p.addVariable(y)

p.appendConstraint(0.25 * x + 0.50 * y <= 120)
p.appendConstraint(0.50 * x + 0.50 * y <= 150)
p.appendConstraint(0.25 * x <= 50)

p.appendObjective(12 * x + 15 *y)

s.solveProblem(p)
print("x =", x.getValue())
print("y =", y.getValue())

