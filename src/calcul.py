import numpy as np

learningRate = 0.1
max_iterations = 5000000
tolerance = 1e-9



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


def calc_gradient(theta, X, Y, F):
	'''
		Calcul the gradient of the cost function.
		Error = diff between calc_linear and real price
		F = matrice [linear regression]
		Y = matrice [price, ]
		X = matrice [mileage n, 1]
		theta = [0, 0]
		gradient[0] = (1/m) * sum(Error)
		gradient[1] = (1/m) * sum(Error * X)
	'''
	Error = F - Y
	gradient = (1/Y.size) * (X.T @ Error)
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



def cost_function(F, Y):
	'''
		This function calculate our program cost error
		It is near the MSE calcul except we divided by 2m 
	'''
	Error = F - Y
	cost = (Error ** 2).sum() / (2 * Y.size)
	return cost


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

	for i in range(max_iterations):
		F = calc_linear(X, theta).reshape(-1,1)
		gradient = calc_gradient(theta, X, Y, F)

		if not np.isfinite(gradient).all():
			print("Training stopped : gradient is not finite.")
			print("Gradient :", gradient)
			print("Iterations :", i)
			return None
		elif np.linalg.norm(gradient) < tolerance:
			print("Training stopped : gradient converged.")
			print("Gradient norm :", np.linalg.norm(gradient))
			print("Iterations :", i)
			return theta
		tmptheta = gradient * learningRate
		theta = theta - tmptheta
	print("Training stopped : max iterations.")

	return theta
