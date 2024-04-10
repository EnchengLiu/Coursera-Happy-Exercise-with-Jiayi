import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Initialize
N = 10**4
x0 = np.random.uniform(-1, 1, N)
v0 = np.random.uniform(-1, 1, N)
w0 = np.random.uniform(-1, 1, N)

# Propagate the particles
x1 = x0 + v0
z1= 1

weights = uniform.pdf(z1 - x1, -1, 2)  # The probability of the observation given the particle
print(z1 - x1)
print(weights)

# Normalize the weights
weights /= np.sum(weights)
print(weights)

# Resample the particles
indices = np.random.choice(np.arange(N), size=N, p=weights)
print(indices)
x1_resampled = x1[indices]

# Plot the histogram of the resampled particles
plt.hist(x1_resampled, bins=50, density=True, label='Particles')

# Plot the analytical solution
x_m = np.linspace(-0, 2, 1000)
pdf = 1-0.5*x_m 
plt.plot(x_m , pdf, label='Analytical solution')

plt.legend()
plt.show()