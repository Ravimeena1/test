lst=[]
lst1=[1,2,3,4,5,6,7,8,9,10]
def filter(lst1):

    for i in lst1:
        if i%2==0:
            lst.append(i)
    return lst
print(filter(lst1))
