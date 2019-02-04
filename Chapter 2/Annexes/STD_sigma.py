import math

def mean(l):
    s=0
    for i in l:
        s = s +(i[0] * i[1])
    return s

"""
Computing the Standrad Deviation. Using a list of Tuples.

"""
def std(l):

    s = 0
    mu = mean(l)

    for i in l:
        s = s + (((i[0] - mu)**2) * i[1] )

    return math.sqrt(s)




t = []
x= (0,0.2)
t.append(x)
t.append((137,0.55))
t.append((170,0.25))

print(t)
print(mean(t))
print(std(t))
