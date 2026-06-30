from parsing import load_csv

def main():
	""" 
		main program function
		ask for car's mileages as an input, then check validity
		to launch program
	"""

	datas = load_csv("../data.csv")
	# print("Here is datas :\n", datas)
	theta0 = 0
	theta1 = 1
	mileage = datas.km
	print("Here is mileage :\n", mileage)

	
	return

if __name__ == "__main__":
	main()