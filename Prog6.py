import math
n = input()

lst=[]
s = ''
for i in n:
    if i==',':
        lst.append(int(s))
        s=''
        continue
    else:
        s += i
lst.append(int(s))

print(lst)
Q=[]
c=50
c.__floor__()
h=30
for i in lst:
    m=(math.sqrt((2*c*i)/h))

    Q.append(round(m))
print(Q)

