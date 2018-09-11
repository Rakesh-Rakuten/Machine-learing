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
distance=[0]*len(y)

t=np.array([[1,1,-1,-1],[1,-1,1,-1]])
t_class=[]
for p in range(t.shape[1]):
    for i in range(len(x[0])):
        for j in range(d):
            distance[i] = distance[i]+np.power(float(x[j,i])-t[j,p],2)
        distance[i]=np.sqrt(distance[i])
    k=700 #nearest neighbours
    distance_index = np.argsort(distance)[:k]

    c1=0    #class1 has label value 1
    c2=0    #class2 has label value -1
    for k in distance_index:
        if(Y[0,k]=='1.000000000000000000e+00'):
            c1+=1;
        else:
            c2+=1;
    if(c1>=c2):
        t_class.append(1)
    else:
        t_class.append(-1)

print(t_class)









