from numpy import *
m=int(input("enter number of row\n"))
n=int(input("enter number of col\n"))
x=zeros((m,n),dtype=int)
for i in range(m):
    for j in range(n):
        x[i][j]  =i*j



print(x)
