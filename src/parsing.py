from pathlib import Path
import pandas as pd
import numpy as np
from calcul import calc_std_deviation


def parse_input(arg: str):
	"""
		Check if input is a number + normalise it
		Input - str -> string input
		Output -> Normalise mileages, or -1 if error
	"""
	try:
		value = int(arg)
		if value < 0:
			raise ValueError
	except ValueError:
		print("Error validating input : not a mileage")
		return -1
		
	return value


def extract_theta_from_csv(trained_params_path: str):
	"""
		Extract theta values from a CSV file containing trained parameters.
		Args:
			trained_params_path (str): Path to the CSV file containing trained parameters.
		Returns:
			tuple: A tuple containing theta0 and theta1 values if successful, None otherwise.
	"""
	trained_params = load_csv(trained_params_path)
	if trained_params is None or trained_params.empty:
		print("No trained parameters found. Please train the model first.")
		return None
	row = trained_params.iloc[0]
	if "theta0" not in row or "theta1" not in row:
		print("Trained parameters are missing. Please ensure the model is trained correctly.")
		return None
	if not np.issubdtype(type(row["theta0"]), np.number) or not np.issubdtype(type(row["theta1"]), np.number):
		print("Trained parameters are not valid numbers. Please ensure the model is trained correctly.")
		return None
	theta = (float(row["theta0"]), float(row["theta1"]))
	if not np.isfinite(theta).all():
		print("Trained parameters are not valid. Please ensure the model is trained correctly.")
		return None
	return theta


def extract_datas_from_csv(data_path: str):
	"""
		Extract datas from a CSV file containing dataset.
		Args:
			data_path (str): Path to the CSV file containing dataset.
		Returns:
			pd.DataFrame: A DataFrame containing the dataset if successful, None otherwise.
	"""
	datas = load_csv(data_path)
	if datas is None or datas.empty:
		print("No dataset found. Please ensure the data file is present and not empty.")
		return None
	if "km" not in datas.columns or "price" not in datas.columns:
		print("Dataset is missing required columns. Please ensure the data file is formatted correctly.")
		return None
	if not np.issubdtype(datas["km"].dtype, np.number) or not np.issubdtype(datas["price"].dtype, np.number):
		print("Dataset contains non-numeric values. Please ensure the data file is formatted correctly.")
		return None
	if not np.isfinite(datas[["km", "price"]]).all().all():
		print("Dataset contains invalid values. Please ensure the data file is formatted correctly.")
		return None
	if (datas[["km", "price"]] < 0).any().any():
		print("Dataset contains negative values. Please ensure the data file is formatted correctly.")
		return None
	return datas

def standard_data(data):
	'''
		This function is here to standardise data from Dataset.
		Standardisation take standard deviation and dataset mean to modify data
		a data superior to mean will be set to positive, and a data inferior will be negative
		Standardisation differ from normalisation because it keeps standard_deviation in datas

		Input : 	data - dataset
		Output :	data - Modified dataset
					mean
					std_deviation
	'''
	km = data.km
	mean = km.sum() / km.size
	max_km = np.nanmax(km)
	min_km = np.nanmin(km)

	std_deviation = calc_std_deviation(km, mean)

	data.km = (km - mean) / std_deviation 

	return data, mean, std_deviation

def unstandard_data(theta, mean, std_deviation):
	'''
		This function is here to unstandardise thetas from Dataset.
		Unstandardisation take standard deviation and dataset mean to modify thetas
		a theta superior to mean will be set to positive, and a theta inferior will be negative
		Unstandardisation differ from normalisation because it keeps standard_deviation in datas

		Input : 	theta - thetas
					mean
					std_deviation
		Output :	theta - Modified thetas
	'''
	tmp_theta = theta.copy()
	tmp_theta[0] = theta[0] - (theta[1] * mean / std_deviation)
	tmp_theta[1] = theta[1] / std_deviation
	theta = tmp_theta
	return theta

def load_csv(path: str) -> pd.DataFrame:
	''' 
		Load a file from path, and return infos into Datafram
		input : path - filename to open, which need to be a csv
		output : Dataframe with csv informations
		'''
	try:
		if not path.endswith("csv"):
			raise TypeError("Error, file isn't in csv format")
		data = pd.read_csv(path)
		print("Loading dataset of dimensions", data.shape)
		return data
	except Exception:
		return None


def create_file(theta, mean, std_deviation, filename="models/trained_params.csv"):
	'''
		Create a Csv file using trainings datas
		File is named : trained_params.csv
	'''
	path = Path(filename)
	try:
		path.parent.mkdir(parents=True, exist_ok=True)
		params = pd.DataFrame([{
			"theta0": theta[0],
			"theta1": theta[1]
		}])
		params.to_csv(path, index=False)
	except Exception as e:
		print("Error creating model parameters in {path} : {e}")
	return