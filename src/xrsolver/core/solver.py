import abc

from .constants import Optimization
from .problem import Problem

class SolverProblem:
	def __init__(self):
		self.symbols = []
		self.variables = []
		self.constraints = []
		self.objectives = []
		self.solutions = {}

	def getSymbols(self):
		return self.symbols

	def getVariables(self):
		return self.variables

	def getConstraints(self):
		return self.constraints

	def getMaximizeObjective(self):
		objective = sum(objective[1] if objective[0]==Optimization.Maximize else -1 * objective[1] for objective in self.objectives)
		return objective

	def getMinimizeObjective(self):
		objective = sum(objective[1] if objective[0]==Optimization.Minimize else -1 * objective[1] for objective in self.objectives)
		return objective

	def queryVariableBySym(self, sym):
		return self.variableMap[sym]

	def setSymbolsAndVariables(self, symbols, variables):
		self.symbols = symbols
		self.variables = variables
		self.variableMap = dict(zip(symbols, variables))

	def setConstraints(self, constraints):
		self.constraints = constraints

	def setObjectives(self, objectives):
		self.objectives = objectives

class SolverProblemConverter:
	def __init__(self, solver):
		self.solver = solver
		self.solverVariableMap = {}

	def getSolverVariable(self, symbol):
		return self.solverVariableMap[symbol]

	def convert(self, problem):
		solverProblem = SolverProblem()

		symbols = []
		variables = []

		variableCounter = 0
		for variable in problem.getVariables():
			variableName = "x{0}".format(variableCounter)
			variableCounter += 1
			lb = variable.getLowerBound()
			ub = variable.getUpperBound()
			solverVariable = self.solver.generateSolverVariable(variableName, lb, ub)

			symbol = variable.getSymExpr()
			self.solverVariableMap[symbol] = solverVariable
			symbols.append(symbol)
			variables.append(solverVariable)

		constraints = [self.convertSymExpr(constraint.getSymExpr()) for constraint in problem.getConstraints()]
		objectives = [(objective.getOptimization(), self.convertSymExpr(objective.getFunction().getSymExpr())) for objective in problem.getObjectives()]

		solverProblem.setSymbolsAndVariables(symbols, variables)
		solverProblem.setConstraints(constraints)
		solverProblem.setObjectives(objectives)
		return solverProblem

	def convertSymExpr(self, symExpr):
		if symExpr.is_Number:
			return float(symExpr)
		elif symExpr.is_Relational:
			from .symbol import Le, Lt, Ge, Gt, Eq
			lhsConverted = self.convertSymExpr(symExpr.lhs)
			rhsConverted = self.convertSymExpr(symExpr.rhs)

			if isinstance(symExpr, Eq):
				return self.solver.constraintEq(lhsConverted, rhsConverted)
			elif isinstance(symExpr, Lt):
				return lhsConverted < rhsConverted
			elif isinstance(symExpr, Le):
				return lhsConverted <= rhsConverted
			elif isinstance(symExpr, Gt):
				return lhsConverted > rhsConverted
			elif isinstance(symExpr, Ge):
				return lhsConverted >= rhsConverted

		elif symExpr.is_Symbol:
			return self.getSolverVariable(symExpr)

		elif symExpr.is_Add:
			(c, exprs) = symExpr.as_coeff_add()
			r=self.convertSymExpr(c)
			for e in exprs:
				r = r+self.convertSymExpr(e)
			return r
		elif symExpr.is_Mul:
			(c, exprs) = symExpr.as_coeff_mul()
			r=self.convertSymExpr(c)
			for e in exprs:
				r = r*self.convertSymExpr(e)
			return r
		elif symExpr.is_Pow:
			(base, exp)=symExpr.as_base_exp()
			baseVariable = self.convertSymExpr(base)
			expValue = self.convertSymExpr(exp)
			return pow(baseVariable, expValue)
		else:
			return None

class AbsSolver(object, metaclass=abc.ABCMeta):
	def __init__(self):
		pass

	def generateSolverVariable(self, totalName, lowerBound=None, upperBound=None):
		raise NotImplementedError('users must define generateSolverVariable() to use this base class')

	def constraintEq(self, lhs, rhs):
		return lhs==rhs

	def solveProblem(self, problem: Problem):
		problemConverter = SolverProblemConverter(self)

		solverProblem = problemConverter.convert(problem)

		solutions = self.doSolve(solverProblem)

		for variable in problem.getVariables():
			symbol = variable.getSymExpr()
			solverVariable = problemConverter.solverVariableMap[symbol]
			value = solutions[symbol]
			variable.setValue(value)

	def doSolve(self, problem):
		raise NotImplementedError('users must define solve() to use this base class')

