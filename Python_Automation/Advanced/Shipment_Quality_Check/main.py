quantities = []
while True:
	try:
		quantity = int(input("Enter quantity (-1 to stop): "))
		if quantity == -1:
			break
		quantities.append(quantity)
	except ValueError:
		print("Invalid entry skipped.")
if len(quantities) == 0:
	print("No data to evaluate")
elif min(quantities) < 0:
	print("Contains defective items")
elif min(quantities) >= 0:
	print("All quantities acceptable")
