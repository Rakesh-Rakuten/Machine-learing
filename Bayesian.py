import csv
import numpy as np


def get_input(file):
    with open(file,'r') as f:
        a = csv.reader(f)
        return list(a)


y = get_input('Y.csv')
x = get_input('X.csv')
x = np.array(x)
d = len(x)   #dimension of input

Y = np.array(y).reshape(1,len(y))

c1_mean=[0]*d
c2_mean=[0]*d
c1_var=[0]*d
c2_var=[0]*d

for j in range(d):
    count1=0
    count2=0
    s1=0
    s2=0
    s3=0
    s4=0
    for i in range(len(y)):
        if(Y[0,i]=='1.000000000000000000e+00'):
            count1+=1
            s1+=float(x[j,i])
            s2+=np.power(float(x[j,i]),2)
        else:
            count2+=1
            s3+=float(x[j,i])
            s4+=np.power(float(x[j,i]),2)
    c1_mean[j] = s1/count1
    c1_var[j] = s2/count1-np.power(c1_mean[j],2)
    c2_mean[j] = s3/count2
    c2_var[j] = s4/count2-np.power(c2_mean[j],2)
    prob_class1 = count1/len(y)
    prob_class2 = count2/len(y)
print('probability of class 1:',prob_class1)
print('probability of class 2:',prob_class2)
#print('Means:',c1_mean)
#print('variance:',c1_var)
t=np.array([[1,1,-1,-1],[1,-1,1,-1]])    #Taken each test input as columns
fc = []
for p in range(t.shape[1]):
    o1 = 1
    o2 = 1
    for s in range(d):
        o1 =o1*1/np.sqrt(2*np.pi*c1_var[s])*np.exp(-1*np.power((t[s,p]-c1_mean[s]),2)/2*c1_var[s])*prob_class1
        o2 =o2*1/np.sqrt(2*np.pi*c2_var[s])*np.exp(-1*np.power((t[s,p]-c2_mean[s]),2)/2*c2_var[s])*prob_class2
    if(o1>=o2):
        fc.append(1)
    else:
        fc.append(-1)
print("Final class assigned to each test Input is:",fc)
