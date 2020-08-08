from ._data_ import Params, Table
from ._oper_ import gen_table, crc


class Crc:
	@classmethod
	def from_args(cls, name, hash_size, poly, init: int, xor_out: int, ref_in: bool, ref_out: bool):
		return cls(name, Params(hash_size, poly, init, xor_out, ref_in, ref_out))

	@classmethod
	def from_table(cls, name, crc_table: Table):
		return cls(name, crc_table.params)

	def __init__(self, name, crc_params: Params):
		self.name = name
		self.table = gen_table(crc_params)

	def __repr__(self):
		return f"Crc({repr(self.name)}, {repr(self.table.params)})"

	def __call__(self, iterable):
		return crc(iterable, self.table)

	def calc(self, iterable):
		return crc(iterable, self.table)
