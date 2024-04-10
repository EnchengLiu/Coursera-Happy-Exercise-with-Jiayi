#EE-C220C Hw5 Code

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
from scipy.optimize import fsolve

#problem3.1

# Define the parameters
dt=0.1
sigma_a=1

A=np.array([[1,dt],[0,1]])
H=np.array([[1,0]])
P_0=np.eye(2)
# print("P_0=",P_0)   
Sigma_vv=sigma_a**2*np.array([[0.25*dt**4,0.5*dt**3],[0.5*dt**3,dt**2]])
Sigma_ww=np.array([[100]])
#Initial conditions
P_m=[P_0]
P_p=[]
K=[]

print("P_m=",P_m)

for j in range(1,10000):
    # Prediction step
    # print("P_m=",P_m[-1])
    P_p.append(A@P_m[-1]@A.T+Sigma_vv)
    
    # Update step
    K.append(P_p[-1]@H.T@np.linalg.inv(H@P_p[-1]@H.T+Sigma_ww))
    P_m.append((np.eye(2)-K[-1]@H)@P_p[-1]@(np.eye(2)-K[-1]@H).T+K[-1]@Sigma_ww@K[-1].T)

    
print("P_p=",P_p[-1])
print("K=",K[-1])
print("P_m=",P_m[-1])
print("J_p=",np.sqrt(P_m[-1][0,0]))

