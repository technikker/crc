from dataclasses import dataclass


@dataclass
class Params:
	hash_size: int
	poly: int
	init: int
	xor_out: int
	ref_in: bool
	ref_out: bool

	def __iter__(self):
		def gen():
			yield self.hash_size
			yield self.poly
			yield self.init
			yield self.xor_out
			yield self.ref_in
			yield self.ref_out
		return gen()


@dataclass
class Table:
	params: Params
	values: tuple
