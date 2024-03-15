#EE-C220C Hw4-3 Code
#Problem 5-a-ii

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
A=np.array([[0.4,0.3,0.3,0],[0.3,0.4,0.3,0],[0.3,0.3,0.1,0.3],[0,0,0.3,0.7]])
m=7
H=np.eye(4)
Z=np.array([[0,0,0,0],[62.6,29.4,35.9,40.9],[70.3,44.8,38.8,21.9],[73.5,37.3,25.9,18],[77.2,40.1,39,8.8],[73.2,44.1,31.2,23.9],[94.2,43.8,46.9,17.2],[87.4,53.8,39.6,18.6],[89.7,49.9,44,22],[90.4,51.9,42.5,22.9],[94.2,52.1,54.2,17.2]])
d=[30,0,0,0] #Constant

#Initial conditions
Sqrt_20=np.sqrt(20)

R_0=np.random.multivariate_normal([20,40,60,20],np.eye(4)*Sqrt_20)

X_m=np.empty((11,4))
X_m[0] = R_0
X_hat=np.empty((11,4))
C_m=np.empty((11,4))
C_m[0] = np.random.multivariate_normal([7,7,7,7],np.eye(4))

P_m=np.empty((11,4,4))
P_m[0] = np.eye(4)*Sqrt_20

P=np.empty((11,4,4))

#Iterate over the time steps
for k in range(1,11):
    # Prediction step
    Sigma_vv=np.random.multivariate_normal([0,0,0,0],np.eye(4)*np.sqrt(0.1))
    Sigma_ww=np.random.multivariate_normal([0,0,0,0],np.eye(4)*np.sqrt(25))
    X_hat[k] = A @ X_m[k-1] - C_m[k-1] + d
    P[k]=A@P_m[k-1]@A+Sigma_vv
    
    # Update step
    X_m[k]=X_hat[k]+P[k]@H/(H@P[k]@H+Sigma_ww)@(Z[k]-H@X_hat[k])
    P_m[k]=P[k]-P[k]@H/(H@P[k]@H+Sigma_ww)@H@P[k]
    
    C_m[k]=C_m[k-1]+Sigma_vv
    
    # print("at k=",k,"  X_m[k]=",X_m[k], "  P_m[k]=",P_m[k], "  X_hat[k]=",X_hat[k], "P[k]=",P[k])

# Create a new figure

print("X_hat=",X_hat)
plt.figure()
for i in range(X_hat.shape[1]):
    plt.plot(X_hat[:, i], label=f'Column {i+1}')
plt.legend()
plt.xlabel('k')
plt.ylabel('Value')
plt.show()
