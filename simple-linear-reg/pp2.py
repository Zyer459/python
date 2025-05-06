import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('TkAgg')  # or 'Qt5Agg' set backend

df = pd.read_csv('FuelConsumptionCo2.csv')
# skipping understanding data section


#select col/features
cdf = df[['FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
X = cdf.FUELCONSUMPTION_COMB.to_numpy()
y = cdf.CO2EMISSIONS.to_numpy()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3 train model
from sklearn import linear_model
regressor = linear_model.LinearRegression()
regressor.fit(X_train.reshape(-1,1), y_train) # no reshape = valueError: expected 2D got 1D array

# 4 Use the model to make test predictions on the fuel consumption testing data
y_test_ = regressor.predict(X_test.reshape(-1,1))

# 5 model evaluate calc the MSE for the test prediction
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score
print("mean squared error: %.2f" % mean_squared_error(y_test_, y_test))