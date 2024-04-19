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

# Solve the Riccati equation

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
x1_range=np.linspace(-666,666,400)
x2_range=np.linspace(-15,15,200)

# Initialize the reachable region
reachable_region = []
costs = []

# Iterate over the range of initial states
for x1 in x1_range:
    for x2 in x2_range:
        x = np.array([[x1], [x2]])
        u_sum = 0
        # Simulate the system dynamics over 100 time steps
        for i in range(100):
            u = -K[:,:,i] @ x
            x = A @ x + B @ u
            u_sum += np.sum(u**2)
        J = x.T @ S @ x + u_sum
        if J <= 1:
            reachable_region.append([x1, x2])
            costs.append(J[0, 0])  

# Convert the reachable region to a numpy array
reachable_region = np.array(reachable_region)
costs = np.array(costs)

print("Number of reachable states: ", reachable_region.shape[0])
print("Reachable region: ", reachable_region)

# Plot the reachable region
if reachable_region.size > 0:
    # Plot the reachable region
    plt.figure(figsize=(10, 10))
    plt.scatter(reachable_region[:, 0], reachable_region[:, 1], c=costs, s=1, cmap='viridis')
    plt.colorbar(label='Cost J')
    plt.xlabel('x1(0)')
    plt.ylabel('x2(0)')
    plt.title('Reachable Region with Fuel Budget J = 1')
    plt.grid(True)
    plt.show()
else:
    print("No reachable region found with the given fuel budget.")