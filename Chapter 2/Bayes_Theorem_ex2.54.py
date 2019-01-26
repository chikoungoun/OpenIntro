""" General Bayes Theorem

Working on the example 2.54 of the page 98 in the bookself.

We will work following these annotations following the Bayes Theorem example  :

* Basics
************
C = P(C)  : Probability of Having Cancer
notC = P(7C)  : Probability of not Having Cancer
M = P(M+) : Probability that the Mammogram is positive
notM = P(notM+) : Probability that the Mammogram is negative

* And ...
M_C = P(M+|C) : Probability the Mammogram is positive knowing that the patient has Cancer
M_notC = P(M+|7C) : Probability the Mammogram is positive knowing that the patient does not have Cancer


*

"""


"""Bayes Theorem """

""" Tree Diagram Data """
#Cancer probability
C = 0.0035
notC = 1 - C

#Mammogram | Cancer
M_C = 0.89
notM_C = 1 - M_C

#Mammogram | Not Cancer
M_notC = 0.07
notM_notC = 0.93


""" To answer this problem we need to find : P(C|M)"""
# Finding P(C and M+)
C_and_M = M_C * C
print("P(C and M+) : ",C_and_M)

# Finding P(notC and M+ )
notC_and_M = M_notC * notC
print("P(notC and M+) : ",notC_and_M)

#Finding M+
M = C_and_M + notC_and_M
print("P(M+) : ",M)


#Finding P(C|M+) = P(C and M+) / P(M+)
C_M = C_and_M / M
print("P(C|M+) : ",C_M)
