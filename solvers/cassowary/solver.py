from xrsolver.core.solver import AbsSolver

class CassowarySolver(AbsSolver):
	def __init__(self):
		super().__init__()
		self.boundConstraints = []

		from cassowary import SimplexSolver
		self.solver = SimplexSolver()

	def generateSolverVariable(self, variableName, lowerBound=None, upperBound=None):
		from cassowary import Variable
		variable = Variable(variableName)
		if lowerBound is not None:
			self.boundConstraints.append(lowerBound <= variable)
		if upperBound is not None:
			self.boundConstraints.append(variable <= upperBound)
		return variable

	def doSolve(self, problem):
		from cassowary import STRONG

		constraints = tuple(self.boundConstraints) + tuple(problem.getConstraints())
		for constraint in constraints:
			self.solver.add_constraint(constraint)

		self.solver.add_constraint(problem.getMaximizeObjective() >= 2**32, STRONG)

		# Cassowary use incremental solving.
		# It solves the problem during changing constraints.

		solutions = {}
		for symbol in problem.getSymbols():
			variable = problem.queryVariableBySym(symbol)
			value = variable.value
			solutions[symbol] = value

		return solutions

Solver = CassowarySolver
