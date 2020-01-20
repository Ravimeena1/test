class genrator:

    def divisible_by_7(self,n):
        for i in range(n):
            if(i%7==0):
                yield (i)

obj=genrator()

s=obj.divisible_by_7(100)
for i in s:
    print(i)


