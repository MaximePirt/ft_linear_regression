from parsing import parse_input, load_csv
from calcul import calc_linear, build_design_matrix
import numpy as np


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

	theta = 0
	mean = 0
	std_deviation = 0
	trained = True
	try:
		data = load_csv("models/trained_params.csv")
		row = data.iloc[0]
		theta = (float(row["theta0"]), float(row["theta1"]))
		mean = float(row["mean"])
		std_deviation = float(row["std_deviation"])
	except Exception as e:
		print("This program has not been trained yet :", e)
		trained = False



	if trained :
		mileage =  (mileage - mean) / std_deviation 
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