import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats
import math
# Number of training samples
N = 5
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
x_new=np.array(np.insert(x1, 0,1,axis=1))

#Finding weight vector
a=np.matmul(np.transpose(x_new), x_new)
b=np.matmul(np.linalg.inv(a),np.transpose(x_new)) 
w=np.matmul(b,y)
print(w)

#For finding mean and variance
mean=[0]*N
s=0
for i in range(0,N):
    for j in range(0,len(w)):
        mean[i]= mean[i] + (x_new[i,j]*w[j])
    s = s+np.power((y[i]-mean[i]),2)
y_std = math.sqrt(s/N)

for i in range(0,N-1):
    mu = mean[i]
    sigma = y_std
    Dis = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(Dis, scipy.stats.norm.pdf(Dis, mu, sigma))
plt.show()
