s= input()
l=s.split(" ")
l.sort()

dict = {}
for i in l:
    c=l.count(i)
    dict[i]=c

for i in dict:
    print(i,end=" ")
    print (dict[i])


