name = input("Enter student name: ")
grade = int(input("Enter grade level: "))
if grade <= 0:
	print("Invalid grade level. Cannot create badge.")
else:
	badge = name[0] * (grade-1) + name
	print(badge)
