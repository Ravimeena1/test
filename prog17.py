s=input()
list1=[]
s1=''
for i in s:
    if i==',':
        list1.append(s1)
        s1=''
    else:
        s1+=i


for i in range (len(list1)):
    s=''
    s+=list1[i]
    l=len(s)
    spc,up,low,num=0,0,0,0
    for j in s:
        m=ord(j)
        if m>=65 and m<=90:
            up+=1
        elif m >= 97 and m <=122:
            low += 1
        elif m >= 48 and m <=57:
            num+= 1
        elif j=='#' or j=='@' or j=='$':
            spc+=1
    if spc>0 and low>0 and up>0 and num>0 and l>=6 :
        print(s)
