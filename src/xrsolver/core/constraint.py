import abc
import uuid
from enum import Enum

class CompoundConstraint(object, metaclass=abc.ABCMeta):
	def getVariables(self):
		raise NotImplementedError('users must define getVariables() to use this base class')

	def getConstraints(self):
		raise NotImplementedError('users must define getConstraints() to use this base class')

	def getObjectives(self):
		raise NotImplementedError('users must define getObjectives() to use this base class')

