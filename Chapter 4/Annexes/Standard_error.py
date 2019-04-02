import math
""" Standard error function

std : Standard deviation of the population
sample_size : size of the sample

"""

def standard_error(std, sample_size):
    return (std/(math.sqrt(sample_size)))
