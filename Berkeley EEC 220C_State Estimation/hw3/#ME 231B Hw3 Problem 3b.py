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

x=np.random.multivariate_normal(mean=np.zeros(2),cov=P0)
max_y_vari=0
min_y_vari=0

max_var_step=0
min_var_step=0

#Iterating through the time steps
for i in range(1,11):
    #Predicting the state and covariance
    x0_min = np.dot(A0,x0)
    P0 = np.dot(np.dot(A0,P0),A0.T) + Q
    
    #Calculating the Kalman gain
    x=np.dot(A0,x)+np.random.multivariate_normal(mean=np.zeros(2),cov=Q)
    K = (np.dot(P0,H.T))/(np.dot(np.dot(H,P0),H.T)+1)
    z= np.dot(H,x)+np.random.normal(0,1)
    
    #Updating the state and covariance
    x0 = x0_min + np.dot(K,(z-np.dot(H,x0_min)))
    P0 = np.dot((vv - np.dot(K,H)),P0)
    
    #Calculating the y value
    y_mean=np.dot(np.array([1,1]),x0)
    # print(y_mean)
    y_vari=np.dot(np.dot(np.array([1,1]),P0),np.array([1,1]).T)
    
    # print('The mean of y at time step',i,'is',y_mean)
    print('The variance of y at time step',i,'is',y_vari)
    
    if y_vari>-np.inf:
        max_y_vari=y_vari
        max_var_step=i
    if y_vari<np.inf:
        min_y_vari=y_vari
        min_var_step=i
       
print('The maximum variance of y is',max_y_vari,'at time step',max_var_step)