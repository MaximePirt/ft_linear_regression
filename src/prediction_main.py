from parsing import parse_input, extract_theta_from_csv
from calcul import calc_linear, build_design_matrix


def main():
	""" 
		main program function
		ask for car's mileages as an input, then check validity
		to launch program
	"""
	print("Enter car's mileages please")
	try:
		arg = input()
	except (EOFError, KeyboardInterrupt):
		print("\nInput cancelled.")
		return -1

	mileage = parse_input(arg)
	if mileage == -1:
		return -1
	print("Here is input :", mileage)

	trained = True
	theta = extract_theta_from_csv("models/trained_params.csv")
	if theta is None:
		trained = False
		



	if trained :
		X = build_design_matrix(mileage)
		res = calc_linear(X, theta)
		if res < 0:
			res = 0
	else:
		res = 0
	print("Here is your vehicle price :", res)
	
	return

if __name__ == "__main__":
	main()