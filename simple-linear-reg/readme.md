Understand the data
FuelConsumption.csv:
use a fuel consumption dataset, FuelConsumption.csv, which contains model-specific fuel consumption ratings and estimated carbon dioxide emissions for new light-duty vehicles for retail sale in Canada. Dataset source.

MODEL YEAR e.g. 2014
MAKE e.g. VOLVO
MODEL e.g. S60 AWD
VEHICLE CLASS e.g. COMPACT
ENGINE SIZE e.g. 3.0
CYLINDERS e.g 6
TRANSMISSION e.g. AS6
FUEL TYPE e.g. Z
FUEL CONSUMPTION in CITY(L/100 km) e.g. 13.2
FUEL CONSUMPTION in HWY (L/100 km) e.g. 9.5
FUEL CONSUMPTION COMBINED (L/100 km) e.g. 11.5
FUEL CONSUMPTION COMBINED MPG (MPG) e.g. 25
CO2 EMISSIONS (g/km) e.g. 182

task is to create a simple linear regression model from one of these features to predict CO2 emissions of unobserved cars based on that feature.

learning objectives:
	- load data using pandas
	- split data into test and train data sets
	- import a linear regression model from scikit-learn
	- train model with train data set and predict with test data set
	- evaluate model using mean square error

to make requirements.txt = pip freeze > <filename.txt>
to install = pip install -r /path/to/<filename.txt>
