def square(i):
    return i*i
lst=[1,2,3,4,5,6,7,8,9,10]
lst2=list(filter(lambda x:x%2==0,lst))
lst1=list(map(square,lst2))

print(lst1)

