from parsing import parse_input

def calcul_estimate_price(theta0: int, theta1: int, mileage: int) -> int:
	res = theta0 + theta1 * mileage
	return res


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

	theta0 = 0
	theta1 = 0
	res = calcul_estimate_price(theta0, theta1, mileage)
	print("Here is res :", res)
	
	return

if __name__ == "__main__":
	main()