""" General Bayes Theorem"""


"""Bayes Theorem with 2 """

#Cancer probability
C = 0.0035
notC = 1 - C

#Mammogram | Cancer
M_C = 0.89
notM_C = 1 - M_C

#Mammogram | Not Cancer
M_notC = 0.07
notM_notC = 0.93



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
