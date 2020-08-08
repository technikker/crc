from ._data_ import Params, Table


def logical_reverse(source: int, length: int):
	r = 0
	for i in reversed(range(length)):
		r |= (source & 1) << i
		source >>= 1
	return r


def gen_table_value(index, crc_params: Params):
	hash_size, poly, ref_in = crc_params.hash_size, crc_params.poly, crc_params.ref_in
	_mask = ~(-1 << hash_size)
	r = index
	if ref_in:
		r = logical_reverse(r, hash_size)
	elif hash_size > 8:
		r <<= hash_size - 8
	last_bit = 1 << (hash_size - 1)
	for i in range(8):
		if (r & last_bit) != 0:
			r = (r << 1) ^ poly
		else:
			r <<= 1
	if ref_in:
		r = logical_reverse(r, hash_size)
	return r & _mask


TABLE_SIZE = 256


def gen_table(crc_params: Params):
	return Table(crc_params, tuple(gen_table_value(i, crc_params) for i in range(TABLE_SIZE)))


def crc(iterable, crc_table: Table):
	if isinstance(iterable, str):
		iterable = (ord(c) for c in iterable)

	_table_params = crc_table.params
	_table_values = crc_table.values
	hash_size, init, xor_out, ref_out = _table_params.hash_size, _table_params.init, _table_params.xor_out, \
		_table_params.ref_out
	_mask = ~(-1 << hash_size)

	r = logical_reverse(init, hash_size) if ref_out else init
	if ref_out:
		for value in iterable:
			r = _table_values[(r ^ value) & 0xff] ^ (r >> 8)
			r &= _mask
	else:
		to_right = hash_size - 8
		to_right = 0 if to_right < 0 else to_right
		for value in iterable:
			r = _table_values[((r >> to_right) ^ value) & 0xff] ^ (r << 8)
			r &= _mask
	return (r ^ xor_out) & _mask
