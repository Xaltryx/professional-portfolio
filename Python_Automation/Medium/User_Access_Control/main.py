try:
	name = input("Enter username: ")
	role = int(input("Enter role level:"))
	if role == 5 and name != "":
		print("Admin access granted")
	elif role >= 1 and role <=4:
		print("Standard access")
	elif role == 0:
		print("Guest access only")
	else:
		print("Invalid role")
except ValueError:
	print("Please write a proper number.")
