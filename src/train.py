import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from parsing import load_csv, standard_data, create_file, unstandard_data
from calcul import training, calc_linear, build_design_matrix


def visualise(raw_datas, X, theta):
	'''
		This function help visualise our linear regression using our programs datas
		After displaying a graph, it saves it in ouputs/figures folder
	'''
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
	return

def main():
	""" 
		main program function
		ask for car's mileages as an input, then check validity
		to launch program
	"""

	raw_datas = load_csv("data/data.csv")
	if raw_datas is None:
		return 1
	datas = raw_datas.copy()
	

	datas, mean, std_deviation = standard_data(datas)
	print("Here is final datas :\n", datas)
	theta = np.array([0, 0])
	theta = training(datas, theta, mean, std_deviation)
	if theta is None:
		return 1

	theta = unstandard_data(theta, mean, std_deviation)

	X = build_design_matrix(raw_datas.km)

	# Create file and put training variables inside 
	create_file(theta, mean, std_deviation)

	# # Visualisation --------
	# visualise(raw_datas, X, theta)

	print("End of training.")
	return

if __name__ == "__main__":
	main()