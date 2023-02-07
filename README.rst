
.. image:: https://img.shields.io/pypi/v/CRCx.svg
	:target: https://pypi.python.org/pypi/CRCx

.. image:: https://img.shields.io/pypi/l/CRCx
	:target: https://spdx.org/licenses/MPL-2.0.html

.. image:: https://img.shields.io/pypi/pyversions/CRCx.svg
	:target: https://pypi.python.org/pypi/CRCx


CRCx
=======

Extensive Cyclic Redundancy Check

Work in progress...

Examples
----------

..
	Because GitHub doesn't support the include directive the source of
	scripts/examples/simple_tcp_server.py has been copied to this file.

.. code:: python

	import crc_rc3 as crc
	import crc_rc3.catalog
	import crc_rc3.engines.generic
	import crc_rc3.engines.tableized
	import crc_rc3.tables
	import zlib


	data = b"123456789"
	data_a = b"12345"
	data_b = b"6789"
	check = 0xcbf43926  # crc from crc32 algorithm for the str '123456789


	"""
	simple usage
		select cataloged algorithm
		parse your input data
	"""
	calc = crc.create(crc.catalog.crc_32())
	hash_a = calc.calc(data)


	"""
	calculate from multiple strings of input
		via instantiate object from the calculator class
	"""
	calc = crc.create(crc.catalog.crc_32())
	inst = calc()
	inst.process(data_a)  # process, update
	hash_b = inst.final()  # you can check the result halfway through the calculation
	inst.process(data_b)
	hash_c = inst.final()  # result, final


	# todo check if is big endian
	"""
	if you need the hash in bytes
		big endian
	"""
	# hash_d = calc.calc_bytes(data)
	# or
	# hash_e = inst.final_bytes()


	"""
	create the crc table manually
	"""
	# table for crc32
	table = crc.tables.new_lsbf(0x04c11db7, 32)
	# repr it so you can put in your own code
	print(crc.tables.table_repr(32, 80)(table))


	"""
	define your own parameters
		option to select engine algorithm
	"""
	# params for crc32
	params = crc.new(
		# required
		width=32,
		poly=0x04c11db7,
		init=0xffffffff,
		xorout=0xffffffff,
		refin=True,
		refout=True,
		# optional
		name="crc32",
		aliases=("alias_1", "alias_2"),
		desc="description",
		table=table,  # you can manually insert table here to avoid it being
		#  calculated automatically every time your program starts
	)
	calc = crc.create(params)
	hash_f = calc.calc(data)


	"""
	use a different engine
		tableized is fastest engine but creates a table of 256 values
			this is the default
		generic doesn't create a table, but is slower
	"""
	# engine = crc.engines.generic
	engine = crc.engines.tableized
	calc = crc.create(params, engine)
	hash_g = calc.calc(data)


	"""
	use the engine directly
		no 'convenience objects'
	"""
	# NotImplemented


	"""
	test
	"""
	hashes = check, zlib.crc32(data), hash_a, hash_c, hash_f, hash_g
	assert all(h == check for h in hashes)
	print(hashes)


	if __name__ == '__main__':
		pass



Features
--------

...

* 01: ...

Other featues:

* ...

License
-------

CRCx is licensed under `Mozilla Public License`_.

.. External References:
.. _GitHub: https://github.com/technikian/crc
.. _Mozilla Public License: https://github.com/technikian/crc/blob/master/LICENCE
