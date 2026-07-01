import numpy as np

learningRate = 0.0000000000001
max_iterations = 5 000 000

#	x = mileage
# 	y = price
#

def calc_linear(mileage, theta):
	'''
		Calcul the linear regression ax+b from matricial shape
	'''
	return np.dot(mileage, theta)



# tmpθ0 = learningRate * 1/m * S(mX-1 i=0)(estimatePrice(mileage[i]) - price[i])

# tmpθ1 = learningRate * 1/m * S(mX-1 i=0)(estimatePrice(mileage[i]) - price[i]) * mileage[i]


def updt_theta(theta, X, Y, F):
	'''
		Calcul the function error + update thetas
		X = matrice [mileage n, 1]
		Y = matrice [price, ]
		F = matrice [linear regression]
		theta = [0, 0]
		Error = diff between calc_linear and real price
	'''
	Error = F - Y
	tmpTheta0 = learningRate * 1/(Y.size) * Error.sum()
	
	tmpTheta1 = learningRate * 1/(Y.size) * (Error * X).sum()
	# print("Here is tmptheta0 and tmptheta1 : \n", tmpTheta0, tmpTheta1)
	return np.array([tmpTheta0, tmpTheta1])

def training(datas, theta):
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
	# print("Here is starting theta :", theta)
	for i  in range(max_iterations):
		F = calc_linear(X, theta).reshape(-1,1)
		tmptheta = updt_theta(theta, X_design, Y, F)
		theta = theta - tmptheta
		if not i % 100000:
			print("Here is theta :", theta)
		# print("Here is tmp shape", tmptheta.shape)
		# print("Here is theta shape", theta.shape)
		# print("Here is theta now :", theta)
	print("\n---\nHere is final theta :", theta)
	res = calc_linear([1, 240000], theta)
	print("Res after training :", res)
	res2 = calc_linear([1, 68500], theta)
	print("Res2 after training :", res2)

	return 0
