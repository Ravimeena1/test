n=input()
lst=[]
s=''
for i in n:
     if i==',':
         m=int(s)
         if m%2!=0:
             lst.append(s)
         s=''

     else:
         s+=i
lst.append(s)
print(lst)
s=''

for i in range(len(lst)):

    s+=lst[i]
    s+=" "
print(s)
