from numpy import math

# pi**2/6= sum(1/n**2) from 1 to infinity

def pi(iteration):
    sum = 0
    for i in range(iteration):
        sum = sum + 1/(i+1)**2
        pi = math.sqrt(6*sum)
    return pi
