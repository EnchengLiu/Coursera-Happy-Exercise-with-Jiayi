#EE-C220C Hw4 Code
#Problem 5-a-ii

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
A=1
m=7
H=1
Z=np.array([0,32.1,39.8,45.9,52.0,51.0,63.4,58.1,60.3,76.6,73.0])
d=10 #Constant
#Initial conditionsS
R_0=np.random.normal(20,5)
X_m=np.empty(11)
P_m=np.empty(11)
X_m[0] = R_0
P_m[0] = 5
X_hat=np.empty(11)
P=np.empty(11)

#Iterate over the time steps
for k in range(1,11):
    # Prediction step
    Sigma_vv=np.random.normal(0,3)
    Sigma_ww=np.random.normal(0,5)
    X_hat[k]=A*X_m[k-1]-m+d
    P[k]=A*P_m[k-1]*A+Sigma_vv
    
    # Update step
    X_m[k]=X_hat[k]+P[k]*H/(H*P[k]*H+Sigma_ww)*(Z[k]-H*X_hat[k])
    P_m[k]=P[k]-P[k]*H/(H*P[k]*H+Sigma_ww)*H*P[k]
    print("at k=",k,"  X_m[k]=",X_m[k], "  P_m[k]=",P_m[k], "  X_hat[k]=",X_hat[k], "P[k]=",P[k])

plt.figure(figsize=(10, 6))
plt.plot( X_hat, marker='o')
plt.title('estimate actual volume of water r for k')
plt.xlabel('k')
plt.ylabel('X_m[k]')
plt.grid(True)
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), np.sqrt(P[1:11]), marker='o')
plt.title('Uncertainty of X_hat')
plt.xlabel('k')
plt.ylabel('Uncertainty')
plt.grid(True)
plt.show()
