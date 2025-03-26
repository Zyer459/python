import numpy as np
import csv

#In Python, the with statement replaces a try-catch block with a concise shorthand. More importantly, it ensures closing resources right after processing them. A common example of using the with statement is reading or writing to a file
# loading csv file 1. read file
def load_file():
	with open ('data.csv', 'r', encoding='ISO-8859-1') as file:
		reader_obj = csv.reader(file, delimiter = ',')
		data = list(reader_obj) # convert the obj to list
		return data

# 2. convert to numpy array
#data_array = np.array(data, dtype = object) #file has string+numbers so use object type
'''However, this will create an array of strings. If your CSV file contains numerical data, you’ll want to convert these strings to the appropriate numerical type. You can do this by specifying the dtype parameter in the np.array function.'''
#print (data_array[:5])
