import numpy as np
from parsing import extract_theta_from_csv, extract_datas_from_csv
from calcul import estimate_price

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
	theta = extract_theta_from_csv("models/trained_params.csv")
	if theta is None:
		return 1
	datas = extract_datas_from_csv("data/data.csv")
	if datas is None:
		return 1


	km = np.array(datas.km)
	price = np.array(datas.price)

	# Evaluations --
	Error = estimate_price(km, theta[0], theta[1]) - price

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