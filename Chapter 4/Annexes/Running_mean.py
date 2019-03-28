""" Running mean method using lists """


""" Sum of a list """
def sum(l):
    s = 0
    for i in l:
        s = s + i
    return s

""" Running Mean """

def running_mean(l):
    tr = []

    for c,i in enumerate(l[:-1]):
        tr.append(sum(l[0:c+1])/(c+1))

    return tr


#Testing it
t = np.arange(1,30)
print(running_mean(t))
