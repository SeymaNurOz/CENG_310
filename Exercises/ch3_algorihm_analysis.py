"""
Created on Sat Apr  9 11:03:13 2022

@author: seyma
R-3.5

"""

# R-3.1 Graph the functions 8n, 4nlogn, 2n*2, n*3, and 2**n using a logarithmic scale
# for the x- and y-axes; that is, if the function value f(n) is y, plot this as a
# point with x-coordinate at logn and y-coordinate at logy.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Uniformly sample 50 x values between -2 and 2:
# x = np.linspace(0,10,100)
# x =np.log2(x)
# # Plot y = x
# plt.plot(x, 8*x, label='$y=8x$')
# plt.plot(x, 4*x*np.log2(x), label='$y=4x.logx$')
# # Plot y = x^2
# plt.plot(x, 2*x**2, label='$y=2x^2$')
# # Plot y = x^3
# plt.plot(x, x**3, label='$y=x^3$')
# # Set the labels for x and y axes:
# plt.plot(x,2**x,label="$y=2^n$")
# plt.xlabel('logx')
# plt.ylabel('logy')
# Create a legend
# plt.legend()

# R-3.5-Explain why the plot of the function nc is a straight line with slope c on a
# log-log scale.

# x = np.linspace(0,5)
# plt.loglog(x, x**8)
# plt.legend()

# R-3.34 There is a well-known city (which will go nameless here) whose inhabitants have the reputation of enjoying a meal only if that meal is the best
# they have ever experienced in their life. Otherwise, they hate it. Assuming meal quality is distributed uniformly across a person’s life, describe
# the expected number of times inhabitants of this city are happy with their
# meals?
n=10
x=list(range(0,10))

print(x)

# P-3.55 Perform an experimental analysis of the three algorithms prefix average1,
# prefix average2, and prefix average3, from Section 3.3.3. Visualize their
# running times as a function of the input size with a log-log chart.
    
def prefix_average1(S):
    n = len(S)
    A = [0]*n # create new list of n zeros
    for j in range(n):
        total = 0 # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1) # record the average
    return A


def prefix_average2(S):
    n = len(S)
    A = [0]* n # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1) # record the average
    return A

def prefix_average3(S):
    n = len(S)
    A = [0]* n # create new list of n zeros
    total = 0 # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j] # update prefix sum to include S[j]
        A[j] = total / (j+1) # compute average based on current sum
    return A

S=[]
for i in range(0,1000):
    S.append(i)
print(S)
import time
start_time = time.time()
prefix_average1(S)
print("--- %s seconds ---" % (time.time() - start_time))
prefix_average2(S)
print("--- %s seconds ---" % (time.time() - start_time))
prefix_average3(S)
print("--- %s seconds ---" % (time.time() - start_time))

    

    



