from parsing import parse_input

def main():
	""" 
		main program function
		ask for car's mileages as an input, then check validity
		to launch program
	"""
	print("Enter car's mileages please")
	arg = input()

	mileage = parse_input(arg)
	if mileage == -1:
		return -1
	print("Here is input :", mileage)
	
	return

if __name__ == "__main__":
	main()