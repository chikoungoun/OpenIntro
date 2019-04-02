import math
""" Confidence Interval of 95%  Function

mean = the population mean
std = standard deviation of the population
sample_size = size of the sample

"""


def ci_95(mean, std, sample_size):
    z = 1.96
    #needs the standard_error
    standard_error(std,sample_size)
    ci_minus = mean - (z * se)
    ci_plus = mean + (z * se)
    ci = (ci_minus,ci_plus)
    #returns a tuple
    return ci

#Standard error method that comes into computation
def standard_error(std, sample_size):
    return (std/(math.sqrt(sample_size)))
