def intTo_string(n):
    s=''
    list=['0','1','2','3','4','5','6','7','8','9']
    while n>0:
        s+=list[n%10]
        n=int(n/10)
    return s[::-1]
num=int(input())
num=intTo_string(num)
print(type(num))
print(num)
