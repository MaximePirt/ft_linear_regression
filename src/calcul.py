
#	x = mileage
# 	y = price
#

def calc_linear(mileage, theta):
	return mileage * theta



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
	X = datas.km
	print("Here is X and theta :")
	print(X)
	print(theta)
	# F = calc_linear(X, theta)
	# print("Here is results :\n", F)

	return 0

