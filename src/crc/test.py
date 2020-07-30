
from crc import CRC


TEST_STR = "123456789"


crc_8_args = {  # Algorithm Name: ((Poly, XorIn, XorOut, RefIn, RefOut), (Result, Check Result))
	"CRC-8": ((0x07, 0x00, 0x00, False, False), (0xF4, 0xF4)),
	"CRC-8/CDMA2000": ((0x9B, 0xFF, 0x00, False, False), (0xDA, 0xDA)),
	"CRC-8/DARC": ((0x39, 0x00, 0x00, True, True), (0x15, 0x15)),
	"CRC-8/DVB-S2": ((0xD5, 0x00, 0x00, False, False), (0xBC, 0xBC)),
	"CRC-8/EBU": ((0x1D, 0xFF, 0x00, True, True), (0x97, 0x97)),
	"CRC-8/I-CODE": ((0x1D, 0xFD, 0x00, False, False), (0x7E, 0x7E)),
	"CRC-8/ITU": ((0x07, 0x00, 0x55, False, False), (0xA1, 0xA1)),
	"CRC-8/MAXIM": ((0x31, 0x00, 0x00, True, True), (0xA1, 0xA1)),
	"CRC-8/ROHC": ((0x07, 0xFF, 0x00, True, True), (0xD0, 0xD0)),
	"CRC-8/WCDMA": ((0x9B, 0x00, 0x00, True, True), (0x25, 0x25)),
}

crc_16_args = {
	"CRC-16/CCITT-FALSE": ((0x1021, 0xFFFF, 0x0000, False, False), (0x29B1, 0x29B1)),
	"CRC-16/ARC": ((0x8005, 0x0000, 0x0000, True, True), (0xBB3D, 0xBB3D)),
	"CRC-16/AUG-CCITT": ((0x1021, 0x1D0F, 0x0000, False, False), (0xE5CC, 0xE5CC)),
	"CRC-16/BUYPASS": ((0x8005, 0x0000, 0x0000, False, False), (0xFEE8, 0xFEE8)),
	"CRC-16/CDMA2000": ((0xC867, 0xFFFF, 0x0000, False, False), (0x4C06, 0x4C06)),
	"CRC-16/DDS-110": ((0x8005, 0x800D, 0x0000, False, False), (0x9ECF, 0x9ECF)),
	"CRC-16/DECT-R": ((0x0589, 0x0000, 0x0001, False, False), (0x007E, 0x007E)),
	"CRC-16/DECT-X": ((0x0589, 0x0000, 0x0000, False, False), (0x007F, 0x007F)),
	"CRC-16/DNP": ((0x3D65, 0x0000, 0xFFFF, True, True), (0xEA82, 0xEA82)),
	"CRC-16/EN-13757": ((0x3D65, 0x0000, 0xFFFF, False, False), (0xC2B7, 0xC2B7)),
	"CRC-16/GENIBUS": ((0x1021, 0xFFFF, 0xFFFF, False, False), (0xD64E, 0xD64E)),
	"CRC-16/MAXIM": ((0x8005, 0x0000, 0xFFFF, True, True), (0x44C2, 0x44C2)),
	"CRC-16/MCRF4XX": ((0x1021, 0xFFFF, 0x0000, True, True), (0x6F91, 0x6F91)),
	"CRC-16/RIELLO": ((0x1021, 0xB2AA, 0x0000, True, True), (0x63D0, 0x63D0)),
	"CRC-16/T10-DIF": ((0x8BB7, 0x0000, 0x0000, False, False), (0xD0DB, 0xD0DB)),
	"CRC-16/TELEDISK": ((0xA097, 0x0000, 0x0000, False, False), (0x0FB3, 0x0FB3)),
	"CRC-16/TMS37157": ((0x1021, 0x89EC, 0x0000, True, True), (0x26B1, 0x26B1)),
	"CRC-16/USB": ((0x8005, 0xFFFF, 0xFFFF, True, True), (0xB4C8, 0xB4C8)),
	"CRC-A": ((0x1021, 0xC6C6, 0x0000, True, True), (0xBF05, 0xBF05)),
	"CRC-16/KERMIT": ((0x1021, 0x0000, 0x0000, True, True), (0x2189, 0x2189)),
	"CRC-16/MODBUS": ((0x8005, 0xFFFF, 0x0000, True, True), (0x4B37, 0x4B37)),
	"CRC-16/X-25": ((0x1021, 0xFFFF, 0xFFFF, True, True), (0x906E, 0x906E)),
	"CRC-16/XMODEM": ((0x1021, 0x0000, 0x0000, False, False), (0x31C3, 0x31C3)),
}

crc_32_args = {
	"CRC-32": ((0x04C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True), (0xCBF43926, 0xCBF43926)),
	"CRC-32/BZIP2": ((0x04C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, False, False), (0xFC891918, 0xFC891918)),
	"CRC-32C": ((0x1EDC6F41, 0xFFFFFFFF, 0xFFFFFFFF, True, True), (0xE3069283, 0xE3069283)),
	"CRC-32D": ((0xA833982B, 0xFFFFFFFF, 0xFFFFFFFF, True, True), (0x87315576, 0x87315576)),
	"CRC-32/MPEG-2": ((0x04C11DB7, 0xFFFFFFFF, 0x00000000, False, False), (0x0376E6E7, 0x0376E6E7)),
	"CRC-32/POSIX": ((0x04C11DB7, 0x00000000, 0xFFFFFFFF, False, False), (0x765E7680, 0x765E7680)),
	"CRC-32Q": ((0x814141AB, 0x00000000, 0x00000000, False, False), (0x3010BF7F, 0x3010BF7F)),
	"CRC-32/JAMCRC": ((0x04C11DB7, 0xFFFFFFFF, 0x00000000, True, True), (0x340BC6D9, 0x340BC6D9)),
	"CRC-32/XFER": ((0x000000AF, 0x00000000, 0x00000000, False, False), (0xBD0BE338, 0xBD0BE338)),
}


def padded_hex(value, hex_len=2):
	r = hex(value)[2:]
	padding = hex_len - len(r)
	if padding < 0:
		return f"0x{r[:padding]}"
	else:
		while padding != 0:
			r = f"0{r}"
			padding -= 1
		return f"0x{r}"


def gen_calculator(key, value, hash_size):
	return CRC(key, hash_size, *value[0])


crc_8 = {k: gen_calculator(k, v, 8) for k, v in crc_8_args.items()}
crc_16 = {k: gen_calculator(k, v, 16) for k, v in crc_16_args.items()}
crc_32 = {k: gen_calculator(k, v, 32) for k, v in crc_32_args.items()}


def test_calculator(calculator, check_a, check_b):
	value = calculator(TEST_STR)
	print("testing", repr(calculator))
	if value != check_a or value != check_b:
		print("! error:", value, check_a, check_b)
	else:
		# print(value, check_a)
		pass
	return


def test_calculators(calculators, args):
	for k, v in args.items():
		test_calculator(calculators[k], *v[1])
	return


if __name__ == "__main__":
	print("start test")
	test_calculators(crc_8, crc_8_args)
	test_calculators(crc_16, crc_16_args)
	test_calculators(crc_32, crc_32_args)
	print("end test - if no errors printed since 'start test', test was successful")
