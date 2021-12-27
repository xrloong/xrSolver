from xrsolver.core.solver import AbsSolver

class DRealSolver(AbsSolver):
	def __init__(self):
		super().__init__()
		self.boundConstraints = []

	def generateSolverVariable(self, variableName, lowerBound=None, upperBound=None):
		from dreal import Variable
		variable = Variable(variableName, Variable.Real)
		if lowerBound is not None:
			self.boundConstraints.append(lowerBound <= variable)
		if upperBound is not None:
			self.boundConstraints.append(variable <= upperBound)
		return variable

	def doSolve(self, problem):
		from dreal import Minimize
		from dreal import And

		constraints = tuple(self.boundConstraints) + tuple(problem.getConstraints())
		objective = problem.getMinimizeObjective()

		result = Minimize(objective, And(*constraints), 0)

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
