n =int( input("enter a number \n"))
sum,last=0,0
for i in range(4):
     sum+=n+last
     last+=n
     n*=10
print(sum)
