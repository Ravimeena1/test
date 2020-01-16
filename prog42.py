tup=(1,2,3,4,5,6,7,8,9,10)
len1=len(tup)/2
for i in range(len(tup)):
    if i<len1:
        if i!=len1-1:
            print (tup[i], end=" ")
        else:

            print (tup[i])

    else:
      print(tup[i],end=" ")

