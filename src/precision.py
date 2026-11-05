import numpy as np
from parsing import load_csv
from calcul import build_design_matrix, calc_linear

def main():
	'''
		This program calculate how much precise is our AI.
		It takes params from trained_params and our dataset.
		It evaluates programs using MSE, RMSE and MAE.

		MSE - Mean Square Error
		RMSE - Root Mean Square Error
		MAE - Mean Absolute Error
	'''

	# Loading files datas
	trained_params = load_csv("models/trained_params.csv")
	if trained_params is None or trained_params.empty:
		print("No trained parameters found. Please train the model first.")
		return -1
	row = trained_params.iloc[0]
	if "theta0" not in row or "theta1" not in row:
		print("Trained parameters are missing. Please ensure the model is trained correctly.")
		return -1
	if not np.issubdtype(type(row["theta0"]), np.number) or not np.issubdtype(type(row["theta1"]), np.number):
		print("Trained parameters are not valid numbers. Please ensure the model is trained correctly.")
		return -1
	theta = (float(row["theta0"]), float(row["theta1"]))
	if not np.isfinite(theta).all():
		print("Trained parameters are not valid. Please ensure the model is trained correctly.")
		return -1
	datas = load_csv("data/data.csv")


	X = build_design_matrix(datas.km)
	Y = np.array(datas.price, dtype=float).reshape(-1, 1)
	F = calc_linear(X, theta).reshape(-1,1)

	# Evaluations --
	Error = F - Y

	mse = (Error ** 2).mean()
	rmse = np.sqrt(mse)
	mae = np.abs(Error).mean()

	print("Model evaluation completed.")
	print("MSE :", mse)
	print("RMSE :", rmse)
	print("MAE :", mae)

	
	return 0


if __name__ == "__main__":
	main()