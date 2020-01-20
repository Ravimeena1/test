def even_num_by_genarator(n):            
    for i in range(n+1):                 
        if(i%5==0) and (i%7==0):         
            yield (i)                    
                                         
                                         
obj=even_num_by_genarator(100)           
for i in obj:                            
    print(i)                             
