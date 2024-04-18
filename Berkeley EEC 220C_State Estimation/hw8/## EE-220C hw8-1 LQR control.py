## EE-220C hw8-1 LQR control

import numpy as np
import matplotlib.pyplot as plt
from control import lqr, ss,  forced_response

# System matrices
A = np.array([[1, 1], [0, 1]])
B = np.array([[1/200], [1/100]])

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

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  

for i, (name, (Q, R)) in enumerate(costs.items()):
    # Compute the LQR gain
    K, S, e = lqr(A, B, Q, R)
    print(f'{name} LQR gain: {K}')
    print(f'{name} LQR cost, solution of Riccati Equation: {S}')
    print(f'{name} LQR eigenvalues of Riccati Equation: {e}')
    
    # Compute the closed-loop system and its eigenvalues
    A_cl = A - B @ K
    eigvals = np.linalg.eigvals(A_cl)
    print(f'{name} closed-loop eigenvalues: {eigvals}')

    # Simulate the system response
    sys = ss(A_cl, B, np.eye(2), np.zeros((2, 1)))
    T, yout = forced_response(sys, T=t, X0=x0)

    # Plot the results on the same subplot with different colors
    axs[0].plot(T, yout[0], color=colors[i % len(colors)], label=f'{name} position state')
    axs[1].plot(T, yout[1], color=colors[i % len(colors)], label=f'{name} velocity state')
    axs[2].plot(T[:-1], (-K @ yout[:, :-1]).reshape(-1), color=colors[i % len(colors)], label=f'{name} acceleration input')

# Add a legend to each subplot
for ax in axs:
    ax.legend()

# Show the plot
plt.tight_layout()
plt.show()