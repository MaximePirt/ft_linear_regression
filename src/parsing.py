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
			raise Error
	except:
		print("Error validating input : not a mileage")
		return -1
		
	return value



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

def load_csv(path: str) -> pd.DataFrame:
	''' 
		Load a file from path, and return infos into Datafram
		input : path - filename to open, which need to be a csv
		output : Dataframe with csv informations
			TODO: Protect csv inputs
		'''
	try:
		if not path.endswith("csv"):
			raise TypeError("Error, file isn't in csv format")
		data = pd.read_csv(path)
		print("Loading dataset of dimensions", data.shape)
		return data
	except Exception as e:
		print("Error opening dataset :", e)
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
			"theta1": theta[1],
			"mean": mean,
			"std_deviation": std_deviation
		}])
		params.to_csv(path, index=False)
	except Exception as e:
		print("Error creating model parameters in {path} : {e}")
	return