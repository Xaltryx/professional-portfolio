prices = [12.5, 5.0, 19.0, 3.5]
def calc_subtotal(prices):
	try:
		sum = 0
		for i in prices:
			sum += i
		return sum
	except:
		print("Please Write a proper number.")

def calc_tax(subtotal,rate):
	if type(subtotal) == float and type(rate) == float:
		return rate * subtotal

def format_total(total):
	try:
		return str(total)
	except:
		print("Please write a proper number.")
if len(prices) != 0 :
	subtotal = calc_subtotal(prices)
	tax = calc_tax(subtotal,0.1)
	total = tax + subtotal
	str_total = format_total(total)
	print("Subtotal:",subtotal)
	print("Tax:",tax)
	print("Total String:",str_total)
else:
	print("No items to process")
