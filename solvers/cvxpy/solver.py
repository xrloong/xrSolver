from xrsolver.core.solver import AbsSolver

class CvxpySolver(AbsSolver):
	def __init__(self, solver):
		super().__init__()
		self.boundConstraints = []

		self.solver = solver

	@classmethod
	def generateInstanceByECOS(cls):
		from cvxpy import ECOS
		return CvxpySolver(ECOS)

	def generateSolverVariable(self, variableName, lowerBound=None, upperBound=None):
		from cvxpy import Variable
		variable = Variable(name = variableName)
		if lowerBound is not None:
			self.boundConstraints.append(lowerBound <= variable)
		if upperBound is not None:
			self.boundConstraints.append(variable <= upperBound)
		return variable

	def doSolve(self, problem):
		from cvxpy import Problem
		from cvxpy import Maximize, Minimize

		constraints = tuple(self.boundConstraints) + tuple(problem.getConstraints())
		prob = Problem(Maximize(problem.getMaximizeObjective()), constraints)
		prob.solve(self.solver)

		solutions = {}
		for symbol in problem.getSymbols():
			variable = problem.queryVariableBySym(symbol)
			value = variable.value.item()
			solutions[symbol] = value

		return solutions

Solver = lambda: CvxpySolver.generateInstanceByECOS()
