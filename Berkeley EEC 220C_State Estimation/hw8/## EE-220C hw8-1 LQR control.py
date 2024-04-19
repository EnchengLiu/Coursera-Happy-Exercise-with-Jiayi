## EE-220C hw8-1 LQR control
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.linalg import solve_discrete_are as care

# System matrices
A = np.array([[1, 0.1], [0, 1]])
B = np.array([[1/200], [0.1]])

# Cost matrices
costs = {
    'A': (np.diag([2, 0]), 1),
    'B': (np.diag([4, 0]), 1),
    'C': (np.diag([4, 0]), 2),
    'D': (np.diag([2, 2]), 1),
    'E': (np.array([[2, 1], [1, 2]]), 1)
}

# Initial condition and time vector
x0 = np.array([10, 0])
t = np.arange(21)

# Initialize a figure and three subplots
fig, axs = plt.subplots(3)
colors = ['b', 'g', 'r', 'c', 'm']  

def state_space(x, A, B, F):
    return A @ x - B @ F @ x
    

for i, (name, (Q, R)) in enumerate(costs.items()):
    # Solve the Riccati equation  
    E= care(A, B, Q, R)
    print(f'{name} Riccati solution:', E)
    
    # Compute the LQR gain
    F = np.linalg.inv(np.array([[R]])+B.T @ E @ B ) @ B.T @ E @ A
    print(f'{name} LQR gain:', F)
    
    # Compute the closed-loop system and its eigenvalues
    A_cl = A - B @ F
    eigvals = np.linalg.eigvals(A_cl)
    print(f'{name} closed-loop eigenvalues: {eigvals}')

    yout = np.zeros((len(t), len(x0)))
    yout[0, :] = x0
    for j in range(1, len(t)):
        yout[j, :] = state_space(yout[j-1, :], A_cl, B, F)

    # Plot the results on the same subplot with different colors
    axs[0].plot(t, yout[:, 0], color=colors[i % len(colors)], label=f'{name} position state')
    axs[1].plot(t, yout[:, 1], color=colors[i % len(colors)], label=f'{name} velocity state')
    axs[2].plot(t[:-1], (-F @ yout[:-1, :].T).reshape(-1), color=colors[i % len(colors)], label=f'{name} acceleration input')
    print(" ")
    
# Add a legend to each subplot
for ax in axs:
    ax.legend()
plt.tight_layout()
plt.show()