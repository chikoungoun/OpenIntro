"""

Code for computing the mean.
Using a list of tuples.

"""



def mean(l):
    s=0
    for i in t:
        s = s +(i[0] * i[1])
    return s




t = []
x= (0,0.2)
t.append(x)
t.append((137,0.55))
t.append((170,0.25))

print(t)
print(mean(t))
