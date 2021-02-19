from os.path import join as path_join
from ..._f_ import table, calculator
from ._cfg_ import params


def factory(f):
	def wrapper_f():
		name = f.__name__
		return calculator(table(*params[name]))
	return wrapper_f


def get_caller_name(level):
	"""level = 0 returns current function name"""
	from inspect import stack as inspect_stack
	return inspect_stack()[level + 1][3]


def write():
	path = path_join(__file__, "../../_f_.py")
	_a = f"from .gen import {factory.__name__}\n"
	_b = ""
	_c = "\n\n" \
		f"@{factory.__name__}\n" \
		"def \u00ff():\n" \
		"\tpass\n"

	with open(path, "w") as f:
		f.write(_a)
		f.write(_b)
		for k in params:
			f.write(_c.replace("\u00ff", k))
