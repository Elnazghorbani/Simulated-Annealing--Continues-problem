# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 18:33:21 2023

@author: eghorbanioskalaei
"""
#Questions: 
    #what is M???? why we should go all the steps we already did with a different number of M
    #for each i in M, the soltion will be started from the point we were in? Yes, because the values of x and y will be stored for the last move in N, the
    #the tempreture will be decreased and the solutions will be provided from the point we were in.
#comment: since here we have a continues problem, we just defind the steps, since we know every new node that is generated is part of our graph
    
import numpy as np
import matplotlib.pyplot as plt


#initial solution
x = 2
y = 1

z = (x**2 + y - 11)**2 + (x + y**2 - 7)**2

#print(x)
#print(y)
#print(z)


T0 = 1000
M = 300
N = 15
alpha = 0.85
temp = []
of = []
k = 0.1

for i in range(M):
    for j in range(N):
        
        x_rand_1 = np.random.rand()
        x_rand_2 = np.random.rand()
        
        if x_rand_1 >= 0.5:    
            x_step = k* x_rand_2
        else:
            x_step= -k* x_rand_2
            
        y_rand_1 = np.random.rand()
        y_rand_2 = np.random.rand()
        
        if y_rand_1 >= 0.5:
            y_step = k* y_rand_2
        else:
            y_step= -k* y_rand_2
        
        
        temporary_x = x + x_step
        temporary_y = y + y_step

        current_objective= (x**2 + y - 11)**2 + (x + y**2 - 7)**2
        temporary_objective =  (temporary_x**2 + temporary_y - 11)**2 + (temporary_x + temporary_y**2 - 7)**2
        random_number = np.random.rand()
        
        if temporary_objective <= current_objective:
            x = temporary_x
            y = temporary_y
        elif random_number <= 1/ (np.exp(temporary_objective - current_objective)/T0):
                x = temporary_x
                y = temporary_y
        else: 
            x = x
            y = y
        
    temp.append(T0)
    of.append(current_objective)
    T0 = alpha * T0
                            
print(x)
print(y)
print(current_objective)
plt.plot(temp,of)
