import math

""" Function to calculate the Normal distribution following the Gaussian formula"""

def normal_distribution(x,mean,std):
    return 1 / math.sqrt(2*(math.pi*(std**2))) * math.exp(-(((x-mean)**2)/(2*(std**2))))
