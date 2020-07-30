
def logical_reverse(source: int, length: int):
	r = 0
	for i in reversed(range(length)):
		r |= (source & 1) << i
		source >>= 1
	return r


class CRC:
	TABLE_SIZE = 256

	def __init__(self, name, hash_size, poly: int, init: int, xor_out: int, ref_in: bool, ref_out: bool):
		self.name = name
		self.hash_size = hash_size
		self.poly = poly
		self.init = init
		self.xor_out = xor_out
		self.ref_in = ref_in
		self.ref_out = ref_out
		self._mask = ~(-1 << hash_size)  # ulong.MaxValue >> (64 - hash_size)
		self._table = self.gen_table()

	def __repr__(self):
		return f"CRC{repr((self.name, self.hash_size, self.poly, self.init, self.xor_out, self.ref_in, self.ref_out))}"

	def _gen_crc(self, iterable, init: int = 0, offset: int = 0, length: int = -1):
		if length == -1:
			length = len(iterable)
		if isinstance(iterable, str):
			data = (ord(v) for v in iterable[offset:offset + length])
		else:
			data = (int(v) for v in iterable[offset:offset + length])

		crc = init
		if self.ref_out:
			for value in data:
				crc = self._table[(crc ^ value) & 0xff] ^ (crc >> 8)
				crc &= self._mask
		else:
			to_right = self.hash_size - 8
			to_right = 0 if to_right < 0 else to_right
			for value in data:
				crc = self._table[((crc >> to_right) ^ value) & 0xff] ^ (crc << 8)
				crc &= self._mask
		return crc

	def __call__(self, iterable):
		init = logical_reverse(self.init, self.hash_size) if self.ref_out else self.init
		_hash = self._gen_crc(iterable, init)
		return (_hash ^ self.xor_out) & self._mask

	def gen_table(self):
		return tuple(self.gen_table_value(i) for i in range(self.TABLE_SIZE))

	def gen_table_value(self, index):
		r = index
		if self.ref_in:
			r = logical_reverse(r, self.hash_size)
		elif self.hash_size > 8:
			r <<= self.hash_size - 8
		last_bit = 1 << (self.hash_size - 1)
		for i in range(8):
			if (r & last_bit) != 0:
				r = (r << 1) ^ self.poly
			else:
				r <<= 1
		if self.ref_in:
			r = logical_reverse(r, self.hash_size)
		return r & self._mask
