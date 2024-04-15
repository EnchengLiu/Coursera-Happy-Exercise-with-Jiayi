import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import inv
import time

def kalman_filter(z, A, Sigma_vv, H, Sigma_ww):
    # Initialize
    n = len(A)
    x_hat = np.zeros((n, len(z)))
    P = np.zeros((n, n, len(z)))
    x_hat_p = np.zeros(n)
    P_p = np.eye(n)

    # Kalman filter
    for k in range(len(z)):
        # Time update
        x_hat_p = A @ x_hat[:, k-1]
        P_p = A @ P[:, :, k-1] @ A.T + Sigma_vv

        # Measurement update
        K = P_p @ H.T @ inv(H @ P_p @ H.T + Sigma_ww)
        x_hat[:, k] = x_hat_p + K @ (z[k] - H @ x_hat_p)
        P[:, :, k] = (np.eye(n) - K @ H) @ P_p

    return x_hat, P

def particle_filter(Np, z, A, Sigma_vv, H, Sigma_ww):
    # Initialize
    n = len(A)
    estimates = np.zeros((n, len(z)))
    particles = np.random.multivariate_normal(np.zeros(n), np.eye(n), Np)
    weights = np.ones(Np) / Np

    # Initialize Sigma_vv based on the size of A
    Sigma_vv = np.eye(n) * Sigma_vv
    
    
    # Particle filter
    for k in range(len(z)):
        # Propagate particles
        particles = A @ particles.T + np.random.multivariate_normal(np.zeros(n), Sigma_vv, Np).T
        particles = particles.T

        # Update weights based on observation
        weights *= np.exp(-0.5 * np.squeeze((z[k] - H @ particles.T)**2 / Sigma_ww))

        # Normalize weights and handle case where all weights are zero
        if np.sum(weights) == 0:
            weights = np.ones(Np) / Np
        else:
            weights /= np.sum(weights)

        # Resample particles
        indices = np.random.choice(np.arange(Np), size=Np, p=weights)
        particles = particles[indices]

        # Compute estimate
        estimate = np.mean(particles, axis=0)
        estimates[:, k] = estimate

    return estimates

# Measurement sequence
z = np.array([1.0, 0.5, 1.5, 1.0, 1.5])

# System matrices
A_values = [np.array([[1]]), np.array([[1, 1], [0, 1]]), np.array([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])]
H_values = [np.array([[1]]), np.array([[1, 0]]), np.array([[1, 0, 0, 0]])]
Q = np.eye(1)
R = np.eye(1)
print("Q = ", Q,"R = ", R)

# Kalman filter and particle filter
np_values = [1, 10, 100, 1000]


all_dM_values = []
all_time_values = []
    
# For each system
for A, H in zip(A_values, H_values):
    dM_values = []
    time_values = []
    x_hat_kf, P_kf = kalman_filter(z, A, Q, H, R)
    
    for Np in np_values:
        dM_temp = []
        time_temp = []

        # Run the particle filter 100 times
        for _ in range(100):
            start_time = time.time()
            x_hat_pf = particle_filter(Np, z, A, Q, H, R)
            # print("shape of x_hat_pf = ", x_hat_pf.shape)
            
            end_time = time.time()

            # Compute the Mahalanobis distance
            dm = np.sqrt((x_hat_kf[0, -1] - x_hat_pf[0, -1])**2 / P_kf[0, 0, -1])
            # print("dm = ", dm)
            dM_temp.append(dm)

            # Compute the computation time
            time_temp.append(end_time - start_time)

        dM_values.append(np.mean(dM_temp))
        time_values.append(np.mean(time_temp))
        
    # Store the dM_values and time_values for this system
    all_dM_values.append(dM_values)
    all_time_values.append(time_values)

# Plot the Mahalanobis distance for each system
plt.figure()
for i, dM_values in enumerate(all_dM_values):
    plt.loglog(np_values, dM_values, label=f'System {i+1}')
plt.xlabel('Number of particles')
plt.ylabel('Average Mahalanobis distance')
plt.title('Mahalanobis distance between Kalman filter and particle filter')
plt.legend(["a-i","a-ii","a-iii"])
plt.show()

# Plot the computation time for each system
plt.figure()
for i, time_values in enumerate(all_time_values):
    plt.loglog(np_values, time_values, label=f'System {i+1}')
plt.xlabel('Number of particles')
plt.ylabel('Average computation time')
plt.title('Computation time of particle filter')
plt.legend(["a-i","a-ii","a-iii"])
plt.show()