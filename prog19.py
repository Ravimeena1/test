n=int (input("enter the number of input you want enter") )
lst1=[]
for i in range(0,n):
    s= input()
    l=s.split(",")
    t=tuple(l)
    lst1.append(t)
lst1.sort()
print (lst1)

