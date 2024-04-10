import numpy as np
import matplotlib.pyplot as plt

def particle_filter(Np, num_runs=1000):
    estimates = []
    for _ in range(num_runs):
        # Initialize particles
        particles = np.random.uniform(-1, 1, Np)
        weights = np.ones(Np) / Np

        # Propagate particles, x_t = x_{t-1}^3 + v_t
        particles = particles**3 + np.random.uniform(-1, 1, Np)
        # print(particles)

        # Update weights based on observation
        z = 0.5
        weights *= np.exp(-0.5 * (z - particles**3 - np.random.uniform(-1, 1, Np))**2)
        # print("weights: ", weights) 
        weights /= np.sum(weights)

        # Resample particles
        indices = np.random.choice(np.arange(Np), size=Np, p=weights)
        particles = particles[indices]

        # Compute estimate
        estimate = np.mean(particles)
        estimates.append(estimate)

    return estimates

# Run the particle filter for different numbers of particles
np_values = [10, 100, 1000]
estimates = [particle_filter(Np) for Np in np_values]
# print("Estimates: ", estimates) 

# Plot histograms of the estimates
plt.figure(figsize=(10, 6))
for i, Np in enumerate(np_values):
    mean = np.mean(estimates[i])
    std = np.std(estimates[i])
    print(f'Np = {Np}: Mean = {mean}, Std Dev = {std}')
    plt.hist(estimates[i], bins=50, alpha=0.5, label=f'Np = {Np}')
plt.legend()
plt.xlabel('Estimate')
plt.ylabel('Frequency')
plt.title('Histograms of Final Estimates for Different Numbers of Particles for Problem 2')
plt.show()