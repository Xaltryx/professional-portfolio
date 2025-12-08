import random

def generate_scores(n):
	try:
		if n < 0:
			return []
		random_numbers = []
		for i in range(n):
			number = random.randint(1,10)
			random_numbers.append(number)
		print("Scores:",random_numbers)
		return random_numbers
	except TypeError:
		print("Please write a proper number.")
		return []
def analyze(scores):
	if len(scores) == 0:
		print("No scores to analyze")
	else:
		print("Max:",max(scores))
		print("Min:",min(scores))
		print("Count:",len(scores))
numbers = generate_scores(10)
analyze(numbers)
