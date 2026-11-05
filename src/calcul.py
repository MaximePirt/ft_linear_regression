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


def estimate_price(mileage, theta0, theta1):
	'''
		Calcul the price from the subject require
		estimatePrice(mileage) = theta0 + (theta1 * mileage)
	'''
	return theta0 + (theta1 * mileage)



def training(datas):
	'''
		Train a linear regression model with batch gradient descent.
		At each iteration, theta0 and theta1 are updated simultaneously :
			theta0 -= learningRate * mean(error)
			theta1 -= learningRate * mean(error * km)
		with error = estimate_price(km) - price.
		Input :		datas - dataset with 'km' and 'price' columns
		Output :	numpy array [theta0, theta1] when the gradient converged
					(norm < tolerance) or max_iterations is reached,
					None if the gradient becomes non finite (divergence)
	'''

	km = np.array(datas.km, dtype=float)
	price = np.array(datas.price, dtype=float)
	theta0, theta1 = 0.0, 0.0

	
	for i in range(max_iterations):
		error = estimate_price(km, theta0, theta1) - price
		gradient = np.array([error.mean(), (error * km).mean()])

		if not np.isfinite(gradient).all():
			print("Training stopped : gradient is not finite.")
			print("Iterations :", i)
			return None
		elif np.linalg.norm(gradient) < tolerance:
			print("Training stopped : gradient converged.")
			print("Iterations :", i)
			return np.array([theta0, theta1])

		tmp_theta0 = gradient[0] * learningRate
		tmp_theta1 = gradient[1] * learningRate
		theta0 = theta0 - tmp_theta0
		theta1 = theta1 - tmp_theta1
	theta = np.array([theta0, theta1])
	print("Training stopped : max iterations.")

	return theta
