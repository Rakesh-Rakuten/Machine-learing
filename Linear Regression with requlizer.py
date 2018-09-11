import numpy as np
import matplotlib.pyplot as plt

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

#creating ones for Bias
x_new=np.array(np.ones(len(x))).reshape(N,1)

#order of polynomial
m=5
for i in range(1,m+1):
    x_new=np.array(np.insert(x_new, i,np.power(x,i),axis=1))

#regulizer
lamda=0.6

#Finding weight vector
a=np.matmul(np.transpose(x_new), x_new)
b=a+lamda*np.identity(a.shape[0])
b=np.matmul(np.linalg.inv(a),np.transpose(x_new)) 
w=np.matmul(b,y)
print(w)

mean = 0
std = 0.05
#Generate more floats to check the fit
#This corresponds to test data
N_test = 100

x_test = np.linspace(0, 2*np.pi, N_test)

x_test += np.random.normal(mean, std, N_test)

x_test_new=np.array(np.ones(len(x_test))).reshape(N_test,1)

# order of polynomial
for i in range(1,m+1):
    x_test_new = np.array(np.insert(x_test_new,i,np.power(x_test,i),axis=1))

y_hat=np.matmul(x_test_new,w)
plt.plot(x,y,'ro',x_test,y_hat,'g')
plt.show()
