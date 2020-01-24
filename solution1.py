def istrue(pos,A):
    for i in range(pos+1,len(A)):
        if A[pos]>=A[i]:
            return True
    return False


A=[9,10 ,6, 8, 2 ,6, 1, 3 ,4]
B=[1 ,2, 6, 4, 5 ,6 ,9 ,2, 6]
list3=[]
sum=0
for i in range (len(A)-1):
  if  A[i]>A[i+1]:
      sum+=B[i]
  else:
      if istrue(i,A):

         list3.append((A[i]*(sum+B[i])))
      else:

          for j in range(i,len(A)):
              sum+=B[j]

          list3.append(A[i]*(sum))

          break
      sum=0

print(list3)
