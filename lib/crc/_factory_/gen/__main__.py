# from ..gen import crc_factory, crc_params
from crc._factory_.gen import crc_factory, crc_params

if __name__ == "__main__":
	pass

OUTPUT_PATH = "../type.py"
IMPORTS = f"from .gen import {crc_factory.__name__}\n"
CODE_A = "\n\nclass CrcFactory:\n"
CODE_B = "" \
	"\n\t@staticmethod\n" \
	f"\t@{crc_factory.__name__}\n" \
	"\tdef \u00ff():\n" \
	"\t\tpass\n"

with open(OUTPUT_PATH, "w") as f:
	f.write(IMPORTS)
	f.write(CODE_A)
	for k in crc_params:
		f.write(CODE_B.replace("\u00ff", k))
