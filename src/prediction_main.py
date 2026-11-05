from parsing import parse_input, extract_theta_from_csv
from calcul import estimate_price


def main():
	"""
		Entry point of the prediction program.

		Asks the user for a car's mileage and validates it. Then loads the
		trained parameters (theta0, theta1) from models/trained_params.csv
		(falls back to (0, 0) if they are missing) and prints the estimated
		price, clamped to 0 when negative.

		Returns -1 if the input is cancelled or invalid, None otherwise.
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

	theta = extract_theta_from_csv("models/trained_params.csv")
	if theta is None:
		theta = (0, 0)

	res = estimate_price(mileage, theta[0], theta[1])
	if res < 0:
		res = 0
	print(f"Here is your vehicle price : {res:.2f}")
	
	return

if __name__ == "__main__":
	main()