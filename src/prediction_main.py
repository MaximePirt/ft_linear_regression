from parsing import parse_input

def main():
	""" 
		main program function
		ask for car's mileages as an input, then check validity
		to launch program
	"""
	print("Enter car's mileages please")
	mileages = input()

	test = parse_input(mileages)
	if test == -1:
		return -1
	print("Here is input :", test)
	
	return

if __name__ == "__main__":
	main()