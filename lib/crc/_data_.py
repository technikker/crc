from dataclasses import dataclass


@dataclass
class Params:
	hash_size: int
	poly: int
	init: int
	xor_out: int
	ref_in: bool
	ref_out: bool


@dataclass
class Table:
	params: Params
	values: tuple
