from ..._type_ import Crc
from ._data_ import crc_params


def get_caller_name(level):
	"""level = 0 returns current function name"""
	from inspect import stack as inspect_stack
	return inspect_stack()[level + 1][3]


def crc_factory(f):
	def wrapper_f():
		name = f.__name__
		return Crc(name, crc_params[name])
	return wrapper_f
