import pandas as pd

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
	except:
		return None
