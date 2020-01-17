list=[12,24,35,24,88,120,155,88,120,155,130,140,24,18,12]
n=len(list)
lst1=[]
print(n)
for i in range(0,(n-1)):

    for j in range(i+1,n):
        if j==n:
            break

        if list[i] == list[j]:
            list.pop(j)
            n-=1



print(list)


