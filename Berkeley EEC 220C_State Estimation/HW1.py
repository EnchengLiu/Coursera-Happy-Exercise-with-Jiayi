from sympy import *
from sympy.stats import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

# Define symbols
t = Symbol('t')
pdf=2*t*exp(-t**2/1000**2)/1000**2
X = ContinuousRV(t, pdf, set=Interval(0, oo))

cdf_X = cdf(X)

cdf_X_func = lambdify(X, cdf_X(X), 'numpy')


#Generate 10^6 Samples and save them to a file, to save time for future runs
# samples=[]
# for i in range(0,10**6):
#     samples.append(sample(X))
# print("Mean: ", np.mean(samples))
# np.savetxt('samples.txt', samples)

loaded_samples = np.loadtxt('samples.txt')

x_values = np.linspace(-0, 4000, 400)
y_values = cdf_X_func(x_values)

#Problem 5b
print("Problem 5b")
print("Failure days at 1%: ", quantile(X)(0.01))
print("Failure days at 10%: ", quantile(X)(0.1))
print("Failure days at 50%: ", quantile(X)(0.5))
print("Failure days at 99%: ", quantile(X)(0.99))

#Problem 5c
print("Problem 5c")
print("Expected lifetime: ", N(E(X)))
print("Probaility of Failure before the expected lifetime: ", N(cdf_X(E(X))))

#Problem 5d
print("Problem 5d")
print("Variance of lifespan: ", N(variance(X)))
print("Standard Deviation of lifespan: ", N(sqrt(variance(X))))
print("The Range of lifespan thats falls within 1 standard deviation of the mean: ", N(E(X)-sqrt(variance(X))), " to ", N(E(X)+sqrt(variance(X))))

#Problem 5e
print("Problem 5e")
Tm=[1,10,100,1000,10000]
Cm=50
Cr=250

for t_m in Tm:
    Overall_Cost_rate=0
    for Sample_LifeSpan in loaded_samples:
        if Sample_LifeSpan > t_m:
            Overall_Cost_rate+=Cm/t_m
        else:
            Overall_Cost_rate+=Cr/Sample_LifeSpan
    print("Overall Cost Rate for t_m=", t_m, " is: ", Overall_Cost_rate/10**6)
    
#Problem 5f
print("Problem 5f")
t, Tm = symbols('t Tm')
pdf=2*t*exp(-t**2/1000**2)/1000**2
After_Tm=(1-Integral(pdf, (t, 0, Tm)).doit())*Cm/Tm
print("After Tm Cost Expectation is ",After_Tm)
Before_Tm = Integral(Cr*pdf/t, (t, 0, Tm)).doit()
print("Before Tm Cost Expectation is ",Before_Tm)

Overall_Cost_rate=After_Tm+Before_Tm
Overall_Cost_rate_func = lambdify(Tm, Overall_Cost_rate, 'numpy')
result=minimize(Overall_Cost_rate_func, 300)
print("Optimal Tm is ", result.x[0])
print("Optimal Overall Cost Rate is ", result.fun)

#Double Check the result with brute force
floor_Tm_optimal = floor(result.x[0])
for t_m in range(floor_Tm_optimal-10, floor_Tm_optimal+10,1):
    Overall_Cost_rate=0
    for Sample_LifeSpan in loaded_samples:
        if Sample_LifeSpan > t_m:
            Overall_Cost_rate+=Cm/t_m
        else:
            Overall_Cost_rate+=Cr/Sample_LifeSpan
    print("Overall Cost Rate for t_m=", t_m, " is: ", Overall_Cost_rate/10**6)
            

#Problem 5a
plt.plot(x_values, y_values)
plt.title('CDF of Problem 5 Distribution')
plt.xlabel('x')
plt.ylabel('CDF')
plt.grid(True)
plt.show()


