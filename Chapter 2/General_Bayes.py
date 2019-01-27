""" Bayes Theorem Rule """

def bayes(x,nx,y,y_x,y_nx):
    return (x_y*x)/((y_nx*nx)+(y_x*x))


""" Finding P(A|B) with Bayes Theorem """

#Basic Probabilities
A = 0
notA = 1-A

B=0
notB = 1-B

#Conditional probabilities
B_A = 0
notB_A = 1 -B_A

B_notA = 0
notB_notA =1 - B_notA

#A_B = (B_A*A)/((B_notA*notA)+(B_A*A))

def bayes(x,nx,y,y_x,y_nx):
    return (x_y*x)/((y_nx*nx)+(y_x*x))


#ex
