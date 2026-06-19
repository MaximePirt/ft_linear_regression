
def parse_input(str: str):
	"""
		Check if input is a number + normalise it
		Input - str -> string input
		Output -> Normalise mileages, or -1 if error
	"""
	try:
		value = int(str)
		if value < 0:
			raise Error
	except:
		print("Error validating input : not a mileage")
		return -1
		
	return value
