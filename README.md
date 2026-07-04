# ft_linear_regression
Introduction to the basic concepts behind machine learning.  We will create a program that predicts the price of a car by using a linear function trained with a gradient descent algorithm.

## Objective

This project as for goal to implement this function :

`estimatePrice(mileage) = theta0 + theta1 * mileage`

The model is first trained on a price-per-kilometer dataset, and then the learned parameters (`theta0`, `theta1`) are saved for reuse in a prediction program.

## Fonctionnality

- Simple linear regression with a single feature: `km`
- Standardizing the data before training
- Training the model using gradient descent
- Saving the trained parameters to a model file
- A prediction program to estimate the price of a car
- A program to evaluate the model using regression metrics
- Monitoring the cost during training to observe convergence

## Architecture


```text
.
├──src/
│	├── data/
│	│   └── data.csv
│	├── models/
│	│   └── training_datas.csv
│	├── outputs/
│	│	└── figures/
│	│	│	└── regression.pdf #only after training
│	├── calcul.py
│	├── parsing.py
│	├── train.py
│	├── predict.py
│	└─── precision.py
├──.gitignore
└── README.md
```


## Dataset

The dataset contains two columns:

- `km`: the car's mileage
- `price`: the car's price

The goal is to learn the linear relationship between these two variables.

## Preprocessing

Before training, the kilometer values are standardized to improve the stability and convergence speed of the gradient descent.

Formula used:

```text
x_scaled = (x - mean) / std_deviation
```

The `mean` and `std_deviation` values are saved with the model to ensure that prediction and evaluation use exactly the same transformation as training.

## Training

The training process iteratively adjusts `theta0` and `theta1` using gradient descent.

At each iteration:

1. the model calculates the predictions,
2. the error between the prediction and the actual value is measured,
3. the parameters are updated,
4. the cost is recalculated to track convergence.

### Cost Function

The project uses a mean squared error adapted for training:

```text
J(theta) = (1 / (2m)) * Σ(prediction - real_value)^2
```

This feature allows you to verify that training is progressing correctly: the more the cost decreases, the better the model fits the data.

### Early Termination

In addition to setting a maximum number of iterations, training can be stopped when the relative improvement in cost becomes too small.

Example:

```text
improvement = abs(old_cost - cost) / old_cost
```

If this improvement falls below a defined tolerance, the model is considered to have converged.

## Prediction

The prediction program:

1. loads `theta0`, `theta1`, `mean`, and `std_deviation`,
2. retrieves a mileage value as input,
3. applies the same standardization,
4. calculates the estimated price.

This ensures consistency between the data used for training and the data used for prediction.

## Evaluation

A dedicated script is used to measure the model's performance on the dataset.

### Metrics Used

#### MAE

The **Mean Absolute Error** measures the average absolute error between the predictions and the true values.

```text
MAE = (1 / m) * Σ|prediction - real_value|
```

Interpretation: the model's mean error in the same unit as the price.

#### MSE

The **Mean Squared Error** measures the average of the squared errors.

```text
MSE = (1 / m) * Σ(prediction - real_value)^2
```
It penalizes major errors more heavily.

#### RMSE

The **Root Mean Squared Error** is the square root of the MSE.

```text
RMSE = sqrt(MSE)
```

It retains the benefits of the MSE while returning to the same unit as the price.

## Launch the project

### 1. Train the model
```bash
python train.py
```

### 2. Predicting a Price

```bash
python predict.py
```

### 3. Evaluate Accuracy

```bash
python precision.py
```

## Example Pipeline

```text
data.csv
   -> parsing
   -> standardization of km
   -> construction of the design matrix
   -> gradient descent
   -> saving theta0, theta1, mean, std_deviation
   -> prediction / evaluation
```

## Key Points of the Project

- Always use the same `mean` and `std_deviation` for both prediction and evaluation.
- The cost during training is not a final quality metric, but an indicator of convergence.
- The `MAE`, `MSE`, and `RMSE` metrics are used to evaluate the final quality of the model.

## Areas for Improvement

- Add a visualization of the cost curve
- Add unit tests
- Improve error handling for CSV files
- Add a cleaner CLI interface
- Further separate business logic from execution scripts

## Conclusion

This project provides an understanding of the basics of machine learning without using a ready-made regression library: preprocessing, cost function, gradient descent, model saving, prediction, and evaluation.