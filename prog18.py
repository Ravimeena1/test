n=int(input("how many transation you want enter \n"))
sum=0
for i in range(0,n):
    tran_type=input("enter D if you want to deposite /enter W if you want to withdraL amount")
    amount=int(input("enter amount \n"))
    if tran_type=='D' or tran_type=='d':
        sum+=amount
    else:
        sum-=amount
print("your net amount is ",end=": ")
print(amount)
