#EE-C220C Hw6-1 Code
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
from scipy.optimize import fsolve

#Intialization
sigmavv = np.diag([0.3,0.3])
sigmaww = 0.2
x0 = np.random.multivariate_normal([0.5,0.5],np.diag([0.5,0.5]),1)[0]
# x0=np.array([0.5,0.5])
omega=np.random.normal(0,0.2,1)[0]
# omega=0
P0 = np.diag([0.5,0.5])
z1 = 0.5

#Define the system
def q(x1,x2,v1,v2):
    return np.array([np.sin(x1)+np.cos(x2)+v1,np.cos(x1)-np.sin(x2+v2)])
def A(x1,x2):
    return np.array([[np.cos(x1),-np.sin(x2)],[-np.sin(x1),-np.cos(x2)]])
def L(x1,x2):
    return np.eye(2)
def H(x1,x2):
    return np.array([x2,x1])
def h(x1,x2,omega):
    return x2*x1+omega
M=1
Step=1


for i in range(0, Step):
    #Prior Update
    xm0=x0
    Pm0=P0
    print("xm0[0]", xm0[0], "xm0[1]", xm0[1])
    print("shape of Pm0", Pm0.shape, "shape of A(xm0[0],xm0[1])", A(xm0[0],xm0[1]).shape)   
    print("A(xm0[0],xm0[1])", A(xm0[0],xm0[1]))
    xp1hat=q(xm0[0],xm0[1],0,0)
    Pp1=A(xm0[0],xm0[1])@Pm0@A(xm0[0],xm0[1]).T+L(xm0[0],xm0[1])@sigmavv@L(xm0[0],xm0[1]).T
    
    print("L(xm0[0],xm0[1])@sigmavv@L(xm0[0],xm0[1]).T", L(xm0[0],xm0[1])@sigmavv@L(xm0[0],xm0[1]).T)
    print("A(xm0[0],xm0[1])@Pm0@A(xm0[0],xm0[1]).T",A(xm0[0],xm0[1])@Pm0@A(xm0[0],xm0[1]).T)
    
    print("Pp1=",Pp1)
    #Measurement Update
    K1=Pp1@H(xp1hat[0],xp1hat[1]).T/(H(xp1hat[0],xp1hat[1])@Pp1@H(xp1hat[0],xp1hat[1]).T+M*sigmaww)
    print("K1=",K1)
    xm1=xp1hat+K1*(z1-h(xp1hat[0],xp1hat[1],omega))

print("The estimated state is: ", xm1)
    
    




