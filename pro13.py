n=input()
l1,d1=0,0
l=len(n)
for i in n:
    m=ord(i)

    if m>=65 and  m<=90:
        l1+=1

    elif m>=97 and m<=122:
        l1+=1
    elif m>=48 and m<=57:
        d1+=1
print(l1,d1)
