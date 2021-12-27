from xrsolver import AbsSolver

class Z3Solver(AbsSolver):
	def __init__(self):
		super().__init__()
		self.boundConstraints = []


	def generateSolverVariable(self, variableName, lowerBound=None, upperBound=None):
		from z3.z3num import Real
		variable = Real(variableName)
		if lowerBound is not None:
			self.boundConstraints.append(lowerBound <= variable)
		if upperBound is not None:
			self.boundConstraints.append(variable <= upperBound)
		return variable

	def doSolve(self, problem):
		from z3.z3num import Optimize

		variables = problem.getVariables()
		constraints = problem.getConstraints()
		objective = problem.getMaximizeObjective()

		opt = Optimize()
		constraints = tuple(self.boundConstraints) + tuple(problem.getConstraints())
		for c in constraints:
			opt.add(c)

		opt.maximize(objective)
		opt.check()

		model = opt.model()

		solutions = {}
		for symbol in problem.getSymbols():
			variable = problem.queryVariableBySym(symbol)
			value = model[variable]
			solutions[symbol] = float(value.as_decimal(7)) if hasattr(value, 'as_decimal') else 0

		return solutions

Solver = Z3Solver
