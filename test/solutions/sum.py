def sum(num1, num2):
	if not isinstance(num1, int) or not isinstance(num2, int):
		raise TypeError("One or both passed arguments is not an integer.")
	return num1 + num2