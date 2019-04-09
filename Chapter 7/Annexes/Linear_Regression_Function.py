import pandas as pd
import math


""" Function to compute the Linear Regression from a Pandas Dataframe


"""


d = pd.DataFrame({'A':[1,2,3,4,5,6],'B':[6,5,4,3,2,1]})




def linear_regression(x,y):
    #Small control to test the nature of the parameters (Should be dataFrame columns)
    if type(x) and type(y) is pd.Series:
        print('Series')

        df = pd.DataFrame()
        df['X'] = x
        df['Y'] = y
        df['XY'] = df['X']*df['Y']
        df['X_squared'] = df['X']*df['X']
        df['Y_squared'] = df['Y']*df['Y']
        #Let's make this more readable by putting each of the Numerator and Denominator
        A = (df['Y'].sum() * df['X_squared'].sum()) - (df['X'].sum() * df['XY'].sum())
        B = df.shape[0]*df['X_squared'].sum() -(df['X'].sum())**2
        #We calculate the Y-intercept
        y_intercept =  A/B

        #We know calculate the slope
        C = df.shape[0]*df['XY'].sum() - df['X'].sum()*df['Y'].sum()
        D = df.shape[0]*df['X_squared'].sum() - (df['X'].sum())**2

        #separating the Numerator and Denominator makes it more readable
        slope = C/D

        #Gives the whole table
        #print(df)

        return (slope,y_intercept)


    else:
        print('Type should should be Series (a dataframe column)')

print(linear_regression(d['A'],d['B']))
