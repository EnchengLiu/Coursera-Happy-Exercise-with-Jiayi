#EE-C220C Hw6-3 Code
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
from scipy.optimize import fsolve


# #problem 3-a
# #Intialization
# P0 = 4
# x0 = 1
# delta=np.sqrt(P0)

# #Define the system
# def q(x):
#     return (-x+2*abs(x))

# #Prior Update
# s_xm_0_1 = x0 + delta
# s_xm_0_2 = x0 - delta
# s_xp_1_1 = q(s_xm_0_1)
# s_xp_1_2 = q(s_xm_0_2)

# #Measurement Update
# x_phat=(s_xp_1_1+s_xp_1_2)/2
# Pp1 = (s_xp_1_1-x_phat)**2 + (s_xp_1_2-x_phat)**2
# # print("The updated variance is: ", Pp1)
# # print("The updated state is: ", x_phat)



# #problem 3-b
# #Intialization
# P0 = 4
# x0 = 1
# delta=np.sqrt(P0)

# #Define the system
# def q(x):
#     return (x-1)**3

# #Prior Update
# s_xm_0_1 = x0 + delta
# s_xm_0_2 = x0 - delta
# s_xp_1_1 = q(s_xm_0_1)
# s_xp_1_2 = q(s_xm_0_2)
# print("s_xp_1_1: ", s_xp_1_1, "s_xp_1_2: ", s_xp_1_2, "s_xm_0_1: ", s_xm_0_1, "s_xm_0_2: ", s_xm_0_2, "x0: ", x0, "delta: ", delta)

# #Measurement Update
# x_phat=(s_xp_1_1+s_xp_1_2)/2
# Pp1 = (s_xp_1_1-x_phat)**2 + (s_xp_1_2-x_phat)**2
# print("The updated variance is: ", Pp1)
# print("The updated state is: ", x_phat)

#problem 3-b
#Intialization
P0 = 4
x0 = 1
delta=np.sqrt(P0)

#Define the system
def q(x):
    return 3*x

#Prior Update
s_xm_0_1 = x0 + delta
s_xm_0_2 = x0 - delta
s_xp_1_1 = q(s_xm_0_1)
s_xp_1_2 = q(s_xm_0_2)
print("s_xp_1_1: ", s_xp_1_1, "s_xp_1_2: ", s_xp_1_2, "s_xm_0_1: ", s_xm_0_1, "s_xm_0_2: ", s_xm_0_2, "x0: ", x0, "delta: ", delta)

#Measurement Update
x_phat=(s_xp_1_1+s_xp_1_2)/2
Pp1 = (s_xp_1_1-x_phat)**2 + (s_xp_1_2-x_phat)**2
print("The updated variance is: ", Pp1)
print("The updated state is: ", x_phat)



