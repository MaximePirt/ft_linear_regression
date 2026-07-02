import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from parsing import load_csv, standard_data, create_file
from calcul import training, calc_linear
def main():
	""" 
		main program function
		ask for car's mileages as an input, then check validity
		to launch program
	"""

	raw_datas = load_csv("data/data.csv")
	datas = raw_datas.copy()
	
	datas, mean, std_deviation = standard_data(datas)
	print("Here is final datas :\n", datas)
	theta = np.array([0, 0])
	theta = training(datas, theta, mean, std_deviation)
	# Save thetas, mean, std_deviation in csv file



	X_design = np.array((datas.km), dtype=float).reshape(-1, 1)
	onesX = np.ones((X_design.shape[0], 1), dtype=float)
	X = np.concatenate((onesX, X_design), axis=1)

	# Create file and put training variables inside 
	create_file(theta, mean, std_deviation)

	# Visualisation --------
	plt.plot(raw_datas.km, raw_datas.price, 'X')
	plt.grid()
	plt.xlabel('km')
	plt.ylabel('price')
	plt.plot(raw_datas.km, calc_linear(X, theta), color='red')

	figures_dir = Path("outputs/figures")
	figures_dir.mkdir(parents=True, exist_ok=True)

	plt.savefig(figures_dir / "regression.pdf", dpi=300, bbox_inches="tight")
	plt.show()

	print("Here is datas :", raw_datas)
	print("Here is X :", X)

	
	return

if __name__ == "__main__":
	main()