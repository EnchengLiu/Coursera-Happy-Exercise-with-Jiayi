#EE-C220C Hw6-3 Code
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
from scipy.optimize import fsolve


#problem 3-a
#Intialization
P0 = 4
x0 = 1
SampleSize = 1000000

#Define the system
def q(x):
    return (-x+2*abs(x))

#Get the normally distributed samples
samples=np.random.normal(x0,np.sqrt(P0),SampleSize)
results=q(samples)
normal_mean = np.mean(results)
normal_var = np.var(results)
print("Normal mean: ",normal_mean," Normal variance: ",normal_var)

#Get the uniformly distributed samples
# Calculate the bounds
a = -np.sqrt(12*P0) + x0
b = np.sqrt(12*P0) + x0
uniform_samples = np.random.uniform(a,b,SampleSize)
uniform_results = q(uniform_samples)
uniform_mean = np.mean(uniform_results)
uniform_var = np.var(uniform_results)
print("Uniform mean: ",uniform_mean," Uniform variance: ",uniform_var)


# #problem 3-b
# #Intialization
# P0 = 4
# x0 = 1
# SampleSize = 1000000

# #Define the system
# def q(x):
#     return (x-1)**3

# #Get the normally distributed samples
# samples=np.random.normal(x0,np.sqrt(P0),SampleSize)
# results=q(samples)
# normal_mean = np.mean(results)
# normal_var = np.var(results)
# print("Normal mean: ",normal_mean," Normal variance: ",normal_var)

# #Get the uniformly distributed samples
# # Calculate the bounds
# a = -np.sqrt(12*P0) + x0
# b = np.sqrt(12*P0) + x0
# uniform_samples = np.random.uniform(a,b,SampleSize)
# uniform_results = q(uniform_samples)
# uniform_mean = np.mean(uniform_results)
# uniform_var = np.var(uniform_results)
# print("Uniform mean: ",uniform_mean," Uniform variance: ",uniform_var)


# #problem 3-c
# #Intialization
# P0 = 4
# x0 = 1
# SampleSize = 1000000

# #Define the system
# def q(x):
#     return 3*x

# #Get the normally distributed samples
# samples=np.random.normal(x0,np.sqrt(P0),SampleSize)
# results=q(samples)
# normal_mean = np.mean(results)
# normal_var = np.var(results)
# print("Normal mean: ",normal_mean," Normal variance: ",normal_var)

# #Get the uniformly distributed samples
# # Calculate the bounds
# a = -np.sqrt(12*P0) + x0
# b = np.sqrt(12*P0) + x0
# uniform_samples = np.random.uniform(a,b,SampleSize)
# uniform_results = q(uniform_samples)
# uniform_mean = np.mean(uniform_results)
# uniform_var = np.var(uniform_results)
# print("Uniform mean: ",uniform_mean," Uniform variance: ",uniform_var)

