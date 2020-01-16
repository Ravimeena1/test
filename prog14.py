n=input()
up,low=0,0
l=len(n)
for i in n:
    m=ord(i)

    if m>=65 and  m<=90:
        up+=1

    elif m>=97 and m<=122:
        low+=1


print(low,up)
