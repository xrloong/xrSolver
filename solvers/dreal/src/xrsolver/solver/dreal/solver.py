from xrsolver import AbsSolver

class DRealSolver(AbsSolver):
	def __init__(self):
		super().__init__()
		self.boundConstraints = []
		self.eps = 0.0000001

	def generateSolverVariable(self, variableName, lowerBound=None, upperBound=None):
		from dreal import Variable
		variable = Variable(variableName, Variable.Real)
		if lowerBound is not None:
			self.boundConstraints.append(lowerBound - self.eps <= variable)
		if upperBound is not None:
			self.boundConstraints.append(variable <= upperBound + self.eps)
		return variable

	def doSolve(self, problem):
		from dreal import Minimize
		from dreal import And

		constraints = tuple(self.boundConstraints) + tuple(problem.getConstraints())
		objective = problem.getMinimizeObjective()

		result = Minimize(objective, And(*constraints), self.eps)

		variableToSymbolMap = {}
		for symbol in problem.getSymbols():
			variable = problem.queryVariableBySym(symbol)
			variableToSymbolMap[variable] = symbol

		solutions = {}
		for var, interval in result.items():
			symbol = variableToSymbolMap[var]
			solutions[symbol] = interval.mid()

		return solutions

Solver = DRealSolver
