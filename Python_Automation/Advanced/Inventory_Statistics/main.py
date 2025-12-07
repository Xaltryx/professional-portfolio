quantities = []

while True:
	qty = int(input("Enter item quantity (-1 to stop): "))
	if qty == -1:
		break
	quantities.append(qty)

if len(quantities) == 0:
	print("No items received. Cannot calculate statistics.")
else:
	print("Total items:",sum(quantities))
	print("Average quantity:",sum(quantities)/len(quantities))
	print("Maximum quantity:",max(quantities))
	print("Minimum quantity:",min(quantities))
