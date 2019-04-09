
import pandas as pd
import math


""" Function to compute the Slope of a Linear Regression from a Pandas Dataframe

"""

#Compute the Slope
A = 0
B = 0
for i,j in zip(d['A'].values,d['B'].values):
    A = A + (i - d['A'].mean())*(j - d['B'].mean() )
    B = B + ((i - d['A'].mean())**2)


print(A/B)
