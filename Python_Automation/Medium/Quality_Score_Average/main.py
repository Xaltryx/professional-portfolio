count = 0
sum = 0
while True:
	try:
		number = int(input("Enter score: "))
	except:
		print("Please enter a number.")
		continue
	if number < 0 and number != -1:
		continue
	elif number >= 0 and number <= 10:
		sum += number
		count += 1
	elif number == -1:
		if count == 0:
			print("No valid scores to average.")
		elif count > 0:
			print("Average:",sum/count)
		break
