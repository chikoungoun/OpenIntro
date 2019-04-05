import math
""" Confidence Interval of 95%  Function

pe = the point estimate
std = standard deviation of the population
sample_size = size of the sample
conf_lvl = The Confidence level asked for

"""
#Standard error method that comes into computation
def standard_error(std, sample_size):
    return (std/(math.sqrt(sample_size)))


def ci(mean, std, sample_size,conf_lvl):
    z = {80:1.282,85:1.440,90:1.645,95:1.960,99:2.576,99.5:2.807,99.9:3.291}
    #needs the standard_error
    se = standard_error(std,sample_size)
    ci_minus = mean - (z[conf_lvl] * se)
    ci_plus = mean + (z[conf_lvl] * se)
    ci = (ci_minus,ci_plus)
    #returns a tuple
    return ci
