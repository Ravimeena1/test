n = input()

lst=[]
tup=()
s = ''
for i in n:
    if i==',':
        lst.append(s)
        tup = tup+(s ,)
        s=''
        continue
    else:
        s += i
lst.append(s)
tup = tup+(s ,)
print(lst)
print(tup)
