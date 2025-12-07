try:
	ticket = int(input("Enter ticket number: "))
	if ticket > 0:
		print("Valid ticket")
	else:
		print("Invalid ticket")
except ValueError:
	print("Please write a number.")
