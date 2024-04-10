#packages
import numpy as np
from matplotlib import pyplot as plt

#problem 5. a. 2
#definition of parameters
H = np.array([1,0])
A = np.array([[1 ,-1],[0,1]])
d = 10
Z = np.array([0,32.1,39.8,45.9,52.0,51.0,63.4,58.1,60.3,76.6,73.0])

#initialization
xm = np.empty(2,11)
Pm = np.empty(2,22)
xm[0] = np.random.normal(20,5)
Pm[0] = 25
xhat = np.empty(2,11)
P = np.empty(2,22)

#iteration of kalman filter
for k in range(1, 11):
    #prediction step
    sigmavv = np.random.normal(0,3)
    sigmaww = np.random.normal(0,5)
    xhat[k] = A@xm[k-1] - m + d
    P[k] = A@Pm[k-1]@A + sigmavv

     #update step
    xm[k] = xhat[k] + P[k]@H/(H@P[k]@H+sigmaww)@(Z[k]-H@xhat[k])
    Pm[k]=P[k]-P[k]@H/(H@P[k]*H+sigmaww)@H@P[k]


#plotting the estimate the actual volume of water r for k : 1,2,...,10
plt.figure(figsize=(10,10))
plt.plot(xhat,marker='o',label='xhat')
plt.title(" the estimate the actual volume of water r for k : 1,2,...,10")
plt.xlabel("Time step k")
plt.ylabel("the estimate the actual volume of water")
plt.show()

#plotting associated uncertainty which is the square root of P
plt.figure(figsize=(10, 10))
plt.plot(range(1, 11), np.sqrt(abs(P[1:11])), marker='o')
plt.title('Uncertainty of X_hat')
plt.xlabel('k')
plt.ylabel('Uncertainty')
plt.grid(True)
plt.show()