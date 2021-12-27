from xrsolver.core.solver import AbsSolver

class GekkoSolver(AbsSolver):
	def __init__(self):
		super().__init__()

		from gekko import GEKKO
		self.model = GEKKO(remote = False)

	def generateSolverVariable(self, variableName, lowerBound=None, upperBound=None):
		params = {"name": variableName, "value": 0}
		if lowerBound is not None:
			params["lb"] = lowerBound
		if upperBound is not None:
			params["ub"] = upperBound
		return self.model.Var(**params)

	def doSolve(self, problem):
		variables = problem.getVariables()
		constraints = problem.getConstraints()
		objective = problem.getMinimizeObjective()

		model = self.model

		# Ipopt Options
		# https://www.coin-or.org/Ipopt/documentation/node42.html
		model.solver_options = [
			"tol 1.0e-8",
			"compl_inf_tol 1.0e-8",
		]

		# To avoid too few degrees
		extraVariableCount = max(len(variables), len(constraints)) - len(variables)
		for i in range(extraVariableCount):
			model.Var()

		model.Equations(constraints)

		model.Obj(objective)
		model.solve(disp=False)

		solutions = {}
		for symbol in problem.getSymbols():
			variable = problem.queryVariableBySym(symbol)
			value = variable.value[0]
			solutions[symbol] = value

		return solutions

Solver = GekkoSolver
