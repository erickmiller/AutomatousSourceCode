"""
Root object

Format:

"""

import Lexer
from Command import Command
from Root import Root

class SquareRoot(Command):
	def __init__(self):
		super(self.__class__, self).__init__(1)

	def apply_args(self,args):
		return Root().apply_args([" "]+args)