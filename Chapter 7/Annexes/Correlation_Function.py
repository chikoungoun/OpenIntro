"""
Function to compute the correlation coefficient from a pandas dataframe
Takes the equivalent of the X and Y from a pandas Dataframe

"""
import pandas as pd

def zscore(x,mu,sigma):
    return (x-mu)/sigma

def correlation(dx,dy):
    if type(dx) and type(dy)  is pd.Series:
        #Compute the means
        mx = dx.mean()
        my = dy.mean()

        #Compute the standard deviations
        sx = dx.std()
        sy = dy.std()

        #Compute the second part of the equation
        Q=0
        for i,j in zip(dx,dy):
            Q = Q + (zscore(i,mx,sx)*zscore(j,my,sy))

        #multiply with the first part and return the result
        return (1/(dx.shape[0]-1))*Q

    else:
        print('Type should should be Series (a dataframe column)')
