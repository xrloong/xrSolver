from xrsolver.core.solver import AbsSolver

class PuLPSolver(AbsSolver):
	def __init__(self, solver):
		super().__init__()
		self.solver = solver(msg=False)

	@classmethod
	def generateInstanceByGLPK(cls):
		from pulp import GLPK
		return PuLPSolver(GLPK)

	def generateSolverVariable(self, variableName, lowerBound=None, upperBound=None):
		from pulp import LpVariable
		return LpVariable(variableName, lowBound=lowerBound, upBound=upperBound)

	def doSolve(self, problem):
		from pulp import LpProblem
		from pulp import LpMaximize, LpMinimize

		prob = LpProblem("myProb", LpMaximize)

		for constraint in problem.getConstraints():
			prob += constraint

		prob.objective = problem.getMaximizeObjective()

		status = prob.solve(self.solver)

		solutions = {}
		for symbol in problem.getSymbols():
			variable = problem.queryVariableBySym(symbol)
			value = variable.value()
			solutions[symbol] = value

		return solutions

Solver = lambda: PuLPSolver.generateInstanceByGLPK()
