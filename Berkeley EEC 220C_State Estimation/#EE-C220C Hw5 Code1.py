#EE-C220C Hw4 Code
#Problem 5-a-ii

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
A=1.2
H=1
X_0=0
P_0=3
Sigma_vv=2
Sigma_ww=1
#Initial conditions
k=[1,2,10,1000]

for i in k:
    P_m=np.array([P_0])
    P_p=np.array([])
    K=np.array([])
    X_mhat=np.array([X_0])
    X_phat=np.array([])
    for j in range(1,i+1):
        # Prediction step
        X_phat=np.append(X_phat,A*X_0)
        P_p=np.append(P_p,A*P_m[j-1]*A+Sigma_vv)
        # Update step
        K=np.append(K,P_p[-1]*H/(H*P_p[-1]*H+Sigma_ww))
        X_mhat=np.append(X_mhat,X_phat[-1]+K[-1]*(H*X_phat[-1]-X_phat[-1]))
        P_m=np.append(P_m,(1-K[-1]*H)*P_p[-1]*(1-K[-1]*H)+Sigma_ww*K[-1]*K[-1])
        
    print("k=",i,"  X_mhat=",X_mhat[-1], "  P_m=",P_m[-1], "  X_phat=",X_phat[-1], "P_p=",P_p[-1])
    print("The Posterior Varience at %d is %f" %(i,P_m[-1]))
        
