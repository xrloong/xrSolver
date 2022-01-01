import abc
import uuid
from enum import Enum

from .symbol import V

class CompoundConstraint(object, metaclass=abc.ABCMeta):
	def __init__(self, domain = None):
		self.domain = domain

	def generateVariable(self, name, lb = None, ub = None, ndigits = 6):
		variableName = self.domain + "." + name if self.domain != None else name
		return V(variableName, lb = lb, ub = ub, ndigits = ndigits)

	def getVariables(self):
		raise NotImplementedError('users must define getVariables() to use this base class')

	def getConstraints(self):
		raise NotImplementedError('users must define getConstraints() to use this base class')

	def getObjectives(self):
		raise NotImplementedError('users must define getObjectives() to use this base class')

