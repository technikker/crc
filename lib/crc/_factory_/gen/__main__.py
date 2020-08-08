# from ..gen import crc_factory, crc_params
from crc._factory_.gen import crc_factory, crc_params

if __name__ == "__main__":
	pass

OUTPUT_PATH = "../crc_factory.py"
IMPORTS = f"from .gen import {crc_factory.__name__}\n"
CODE = f"\n\n@{crc_factory.__name__}\n" \
	"def \u00ff():\n" \
	"\tpass\n"

with open(OUTPUT_PATH, "w") as f:
	f.write(IMPORTS)
	for k in crc_params:
		f.write(CODE.replace("\u00ff", k))
