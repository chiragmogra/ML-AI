import numpy as np

r=int(input("enter np of rows"))  #for these
que enter 8
c=int(input("enter np of columns"))  # for these que enter 2
arr=[]
a=100  #initial value of array element
i=0
for i in range(r*c):
    arr.append(a)
    a=a+5
arr=np.array(arr)
arr.reshape(r,c)
