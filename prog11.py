n = input()



lst=[]
s = ''
for i in n:
    if i==',':
        lst.append(s)
        s=''
        continue
    else:
        s += i
lst.append(s)






s=''
l1=[]

for i in lst:
    l= len(i)
    sum,c=0,0
    while l>0:
       sum+=  int(i[l-1])*pow(2,c)
       c+=1
       l-=1
    if sum%5==0:
     l1.append(int(i))

print(l1)





