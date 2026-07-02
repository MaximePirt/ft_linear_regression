import numpy as np

learningRate = 0.000005
max_iterations = 5000000

#	x = mileage
# 	y = price
#

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
	tmpTheta0 = learningRate * 1/(Y.size) * Error.sum()
	
	tmpTheta1 = learningRate * 1/(Y.size) * (Error * X).sum()
	return np.array([tmpTheta0, tmpTheta1])

def training(datas, theta, mean, std_deviation):
	''' Linear regression calcul using two matrices
		X is exemple value, theta is variables
		Y is real prices
		X = [m1, m2, m3 , mn],
		theta = [a, b]
		return F result
		F = X . Theta
		'''
	X_design = np.array((datas.km), dtype=float).reshape(-1, 1)
	onesX = np.ones((X_design.shape[0], 1), dtype=float)
	X = np.concatenate((onesX, X_design), axis=1)

	Y = np.array(datas.price, dtype=float).reshape(-1, 1)

	i = 0
	for i  in range(max_iterations):
		F = calc_linear(X, theta).reshape(-1,1)
		tmptheta = updt_theta(theta, X_design, Y, F)
		theta = theta - tmptheta
		if not i % 100000: # TODO: Remove, debug printing only
			print("Here is theta :", theta)


	return theta
