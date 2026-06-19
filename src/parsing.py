
def parse_input(arg: str):
	"""
		Check if input is a number + normalise it
		Input - str -> string input
		Output -> Normalise mileages, or -1 if error
	"""
	try:
		value = int(arg)
		if value < 0:
			raise Error
	except:
		print("Error validating input : not a mileage")
		return -1
		
	return value
