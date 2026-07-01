import numpy as np
import matplotlib.pyplot as plt
from parsing import load_csv
from calcul import training

def main():
	""" 
		main program function
		ask for car's mileages as an input, then check validity
		to launch program
	"""

	datas = load_csv("../data.csv")
	theta = np.array([0, 0])
	F = training(datas, theta)



	# Visualisation --------
	# plt.plot(datas.km, datas.price, 'X')
	# plt.grid()
	# plt.xlabel('km')
	# plt.ylabel('price')
	# plt.show()

	
	return

if __name__ == "__main__":
	main()