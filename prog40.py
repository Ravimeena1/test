lst=[]
def square1():
    for i in range(1,21):
        lst.append(i*i)
    for i in range(5,len(lst)):
        print(lst[i],end=" ")
square1()
