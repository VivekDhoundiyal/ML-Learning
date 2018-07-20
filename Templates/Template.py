"""
Created on Wed Jul  4 01:57:16 2018
@author: VIVEK
"""

#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing Dataset
dataset = pd.read_csv('Data.csv')

#Splitting data into dependent and indepdndent var
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#Splitting data into training set and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#feature scaling the data 
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)"""
#.............................................................................................................
#Start Coding Here




#.............................................................................................................
