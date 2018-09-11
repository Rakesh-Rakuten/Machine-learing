import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats

N = 10
# Generate equispaced floats in the interval [0, 2p]
x = np.linspace(0, 2*np.pi, N)
# Generate noise
mean = 0
std = 0.05
# Generate some numbers from the sine function
y = np.sin(x)
# Add noise
y += np.random.normal(mean, std, N)

#Finding x
x1 = np.array(x).reshape(N,1)
x_new=np.array(np.ones(len(x))).reshape(N,1)

# order of polynomial
m=2
for i in range(1,m+1):
    x_new = np.array(np.insert(x_new,i,np.power(x,i),axis=1))

#Reguilizer
lamda = 0.4

#Finding weight vector
a=np.matmul(np.transpose(x_new), x_new)
b=np.matmul(np.linalg.inv(a),np.transpose(x_new)) 
w=np.matmul(b,y)
print(w)

w_var = 0
for j in range(0,len(w)):
    w_var = w_var + np.power(w[j],2)
w_std = math.sqrt(w_var/N)

for p in range(0,len(w)):
    mu = w[p]
    sigma = w_std
    Dis = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(Dis, scipy.stats.norm.pdf(Dis, mu, sigma))
plt.show()
