def even_num_by_genarator(n):             
    for i in range(n):                    
        if(i%2==0):                       
            yield (i)                     
                                          
                                          
obj=even_num_by_genarator(10)             
for i in obj:                             
    print(i)                              
