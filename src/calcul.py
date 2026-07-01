import numpy as np

#	x = mileage
# 	y = price
#

def calc_linear(mileage, theta):
	return np.dot(mileage, theta)



# tmpθ0 = learningRate * 1/m * S(mX-1 i=0)(estimatePrice(mileage[i]) - price[i])

# tmpθ1 = learningRate * 1/m * S(mX-1 i=0)(estimatePrice(mileage[i]) - price[i]) * mileage[i]


# def updt_theta(theta, )


def training(datas, theta):
	''' Linear regression calcul using two matrices
		X is exemple value, theta is variables
		X = [m1, m2, m3 , mn],
		theta = [a, b]
		return F result
		F = X . Theta
		'''
	X = np.array((datas.km), dtype=int).reshape(-1, 1)
	onesX = np.ones((X.shape[0], 1), dtype=int)
	X = np.concatenate((onesX, X), axis=1)


	# theta = theta[np.newaxis, :]

	print("Here is X and theta :")
	print(X)
	print(theta)
	print("Here is shapes :")
	print(X.shape)
	print(theta.shape)

	F = calc_linear(X, theta)
	print("Here is results :\n", F)

	return 0

