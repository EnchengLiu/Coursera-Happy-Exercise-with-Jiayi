#ME 231B Hw3 Problem 3b
import numpy as np
import matplotlib.pyplot as plt


#defining the matrices
A0 = np.array([[0.8,0.6],[-0.6,0.8]])
P0 = np.array([[3,0],[0,1]])
Q= np.array([[1,0],[0,1]])
vv = np.eye(2)
H = np.array([1,0])

#Initial conditions
x0 = np.array([0,0])
P0= np.array([[3,0],[0,1]])

e_10=np.zeros((10000,2))

#Iterating through the time steps
for i in range(1,10000):
    #Predicting the state and covariance
    x0=np.random.multivariate_normal(mean=np.zeros(2),cov=P0)
    

    P0 = np.dot(np.dot(A0,P0),A0.T) + Q
    
    x0_hat=np.zeros_like(x0)
    for k in range(1,10):
        
        #Calculating the Kalman gain
        x0=np.dot(A0,x0)+np.random.multivariate_normal(mean=np.zeros(2),cov=Q)
        K = (np.dot(P0,H.T)).dot(np.linalg.inv(np.dot(np.dot(H,P0),H.T)+1))
        z= np.dot(H,x0)+np.random.normal(0,1)
        
        #Updating the state and covariance
        x0_min = np.dot(A0,x0_hat)
        P0 = np.dot(np.dot(A0,P0),A0.T) + Q
        x0_hat = x0_min + K*(z - np.dot(H,x0_min))
        P0 = (np.eye(2)-np.dot(K,H)).dot(P0)
        
        H = np.reshape(H, (-1, 1)) if len(H.shape) == 1 else H
        P0 = np.reshape(P0, (-1, 1)) if len(P0.shape) == 1 else P0
        K = (np.dot(P0,H.T)).dot(np.linalg.inv(np.dot(np.dot(H,P0),H.T)+1))
        
        #Calculating the error
        e_10=x0-x0_hat
        e_10[i]=e_10.flatten()
        
#Plotting the error
plt.figure()
plt.subplot(1,2,1)
plt.hist(e_10[:,0],bins=100)
plt.title('Error in x')
plt.grid(True)

plt.subplot(1,2,2)
plt.hist(e_10[:,1],bins=100)
plt.title('Error in y')
plt.grid(True)

plt.show()
print('The mean of the error in x is:',np.mean(e_10[:,0]))