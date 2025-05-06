import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('TkAgg')  # or 'Qt5Agg' set backend


#import the dataset
url ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

#load dataset directly from url with pd
dataframe = pd.read_csv(url)

#verify load with some random data from url
#df.sample() method returns 5 rows from csv file
#print(dataframe.sample(5))
#show details
#print(dataframe.describe())

#select columns/features which are indicative of CO2 emissions
cdf = dataframe[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
#print(cdf.sample(9))

#visualize features, consider histograms of features below
viz = cdf[['CYLINDERS','ENGINESIZE','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
'''viz.hist() #make a histogram of dataframe, viz
plt.show()''' #show the graphs with matplotlib, tkinter

#now make some scatter plots to see how linear the data is
'''plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')#makes a plot graph: relation of emission & fuel usage
plt.xlabel("FUELCONSUMPTION_COMB") #names of x and y axes
plt.ylabel("Emission")
plt.show()''' #generate graphical view

#graph relation of engine size and emission
'''plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.xlim(0,27)
plt.show()'''

#graph relation of cylinder vs emission
'''plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("CYLINDERS")
plt.ylabel("CO2 Emission")
plt.show()'''

#making a simple regression model to predict CO2 emissions based on engine size
X = cdf.ENGINESIZE.to_numpy()
y = cdf.CO2EMISSIONS.to_numpy()
#split the dataset into mutually exclusive traning and testing sets randomly 80% for training and 20% for test
#train the model with the training set and use unseen testing data to estimate its ability to predict
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#The outputs are one-dimensional NumPy arrays or vectors.
'''print(type(X_train), np.shape(X_train), np.shape(X_train))'''

#building the model
from sklearn import linear_model
#create a model obj
regressor = linear_model.LinearRegression()

# train the model on the training data
# X_train is a 1-D array but sklearn models expect a 2D array as input for the training data, with shape (n_observations, n_features).
# So we need to reshape it. We can let it infer the number of observations using '-1'.

regressor.fit(X_train.reshape(-1,1), y_train)
#print coefficients
'''print('Coefficients: ',regressor.coef_[0])''' # with simple linear regression there is only one coefficient, here we extract it from the 1 by 1 array.
'''print('Intercept: ', regressor.intercept_)'''
#Here, __Coefficient__ and __Intercept__ are the regression parameters determined by the model.  
#They define the slope and intercept of the 'best-fit' line to the training data.
#The regression model is the line given by y = intercept + coefficient * x.
# coefficint in the slope

#vizualize model outputs
#You can visualize the goodness-of-fit of the model to the training data by plotting the fitted line over the data.
'''plt.scatter(X_train,y_train,color='blue')
plt.plot(X_train, regressor.coef_*X_train + regressor.intercept_, '-r')
plt.xlabel("Engine size")
plt.ylabel("Co2 emissions")
plt.show()'''
#model evaluation

from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

#use the predict method to make test predictions
'''y_test_ = regressor.predict(X_test.reshape(-1,1))'''

'''print('Mean absloute error: %.2f' % mean_absolute_error(y_test_, y_test))
print("Mean squared error: %.2f" % mean_squared_error(y_test_, y_test))
print("Root mean squared error: %.2f" % root_mean_squared_error(y_test_, y_test))
print("R2-score: %.2f" % r2_score( y_test_, y_test) )'''

# practice problem 1
#plot regression model result over the test data instead the training data, visually evaluate if the result is good
'''plt.scatter(X_test,y_test, color='green')
plt.plot(X_test, regressor.coef_*X_test + regressor.intercept_, '-r')
plt.xlabel("Engine size")
plt.ylabel("Co2 emissions")
plt.show()'''

# practice problem 2
# select fuel consumption from data frame and split into 80/20 train and test data sets
# Use the same random state as previously so you can make an objective comparison to the previous training result
# see file pp2.py
