import math

""" Function to calculate the Normal distribution following the Gaussian formula"""

def normal_distribution(x,mean,std):
    t = []
    for i in x:
        t.append(1 / math.sqrt(2*(math.pi*(std**2))) * math.exp(-(((i-mean)**2)/(2*(std**2)))))
    return t



t = [.1,.2,.3,.4,.5,.6,.7,.8]
mu = 0
sigma = 0.1

print(normal_distribution(t,mu,sigma))
