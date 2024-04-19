## EE-220C hw8-3 LQR control

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_discrete_are

# Define system matrices
A = np.array([[1, 1], [0, 1]])
B = np.array([[0.5], [1]])
S = np.array([[25, 14], [14, 17]])

# Define the cost function
Q = np.zeros((2, 2))  # State cost
R = np.array([[1]]) # Control cost

# Initialize the Ricatti equation with E(N) = S
E = S
K = np.zeros((1, 2, 100))
# Traceback to compute the gain
for i in range(100):
    #from 99 to 0
    gain= np.linalg.inv(R + B.T @ E @ B) @ (B.T @ E @ A)
    #from 99 to 0
    E = Q + A.T @ E @ A - A.T @ E @ B @ np.linalg.inv(R + B.T @ E @ B) @ B.T @ E @ A
    
    # print("gain: ", gain )
    # print("shape: ", gain.shape)
    K[:, :, 100-i-1] = gain
# print("E: ", E)


# Define the range of initial states
x_0=np.array([285,0])

x=[x_0]
u=[]
J_0=1 #fuel budget
J=[1]

# Simulate the system dynamics over 100 time steps
for i in range(100):
    u_i = -K[:,:,i] @ x[-1]
    print(u_i.shape)
    u.append(u_i)
    x_i = A @ x[-1] + B @ u_i
    x.append(x_i)
    J_0 -= np.sum(u_i)**2
    J.append(J_0)

#Plot the result for state x1, x2, the input u and the cost J
# Create a time vector
x = np.array(x)
t = np.arange(101)

# Create a 2x2 subplot layout
fig, axs = plt.subplots(4, 1, figsize=(10, 10))

# Plot x1
axs[0].plot(t, x[:, 0])
axs[0].set_title('State x1')

# Plot x2
axs[1].plot(t, x[:, 1])
axs[1].set_title('State x2')

# Plot u
axs[2].plot(t[:-1], u)  # u has one less element than x and J
axs[2].set_title('Control input u')

# Plot J
axs[3].plot(t, J)
axs[3].set_title('Cost J')

# Display the plot
plt.tight_layout()
plt.show()