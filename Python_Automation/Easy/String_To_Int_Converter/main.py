def convert_to_int(value):
	try:
		return int(value)
	except ValueError:
		return "Conversion error"
print("12",convert_to_int("12"))
print("0",convert_to_int("0"))
print("19",convert_to_int("19"))
print("004",convert_to_int("004"))
print("abc",convert_to_int("abc"))
