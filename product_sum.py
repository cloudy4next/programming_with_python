

def productSum(array, multiplier = 1):
	
	sum = 0
	for elem in array:
		if type(elem) is list:
			sum += productSum(elem,multiplier + 1)
		else:
			sum += elem
	return sum * multiplier