m=0
for i in range(2000,3001):

    m=i
    flag=True
    while m>0:

        rem=m%10
        if rem%2!=0:
            flag=False
            break
        m=int(m/10)
       
    if flag==True:

        lst.append(i)
print(lst)
