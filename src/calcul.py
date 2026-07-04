import numpy as np

learningRate = 0.000005
max_iterations = 5000000



def calc_std_deviation(args, mean):
	'''
		This function calcul dataset standard deviation
		Input : 	args - data which need to be calculate
					mean 
		Output : deviation
	'''
	tmp_var = []
	for i in args:
		tmp_var.append((i - mean) ** 2)
	
	variance = sum(tmp_var)
	variance = variance / len(args)
	deviation = variance ** (1/2)
	return deviation

def calc_linear(mileage, theta):
	'''
		Calcul the linear regression ax+b from matricial shape
	'''
	return np.dot(mileage, theta)


def updt_theta(theta, X, Y, F):
	'''
		Calcul the function error + update thetas
		Error = diff between calc_linear and real price
		F = matrice [linear regression]
		Y = matrice [price, ]
		X = matrice [mileage n, 1]
		theta = [0, 0]
	'''
	Error = F - Y
	gradient = learningRate * (1/Y.size) * (X.T @ Error)
	return gradient.flatten()


def build_design_matrix(args):
	"""
		Build the design matrix for linear regression.
		Convert args values into a 2D column vector and add a
		column of 1s to represent the intercept term.
		Input :		args : multiple values which will be converted
		Output : 	X_design : np.array version of args
					X : X_design with an additionnal 1 colums
	"""

	X_design = np.array((args), dtype=float).reshape(-1, 1)
	onesX = np.ones((X_design.shape[0], 1), dtype=float)
	X = np.concatenate((onesX, X_design), axis=1)

	return X

def training(datas, theta, mean, std_deviation):
	''' Linear regression calcul using two matrices
		X is exemple value, theta is variables
		Y is real prices
		X = [m1, m2, m3 , mn],
		theta = [a, b]
		return F result
		F = X . Theta
		'''

	X = build_design_matrix(datas.km)
	Y = np.array(datas.price, dtype=float).reshape(-1, 1)

	i = 0
	for i  in range(max_iterations):
		F = calc_linear(X, theta).reshape(-1,1)
		tmptheta = updt_theta(theta, X, Y, F)
		theta = theta - tmptheta
		if not i % 100000: # TODO: Remove, debug printing only
			print("Here is theta :", theta)


	return theta
