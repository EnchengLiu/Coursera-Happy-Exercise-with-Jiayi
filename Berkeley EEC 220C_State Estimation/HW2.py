import matplotlib.pyplot as plt
import numpy as np

def cdf(x, q):
    return 1-(1-2*x)*q**2-2*x*q


x = np.linspace(0, 1, 400)
for q in [0.1, 0.5, 0.9]:
    y = cdf(x, q)
    plt.plot(x, y, label=f'q={q}')
plt.legend()
plt.xlabel("wearing state")
plt.ylabel("probaility")
plt.title("The probability of machining quality better than q")
plt.show()