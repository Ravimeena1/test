n = input()                                                         
                                                                    
lst=[]                                                              
s2=set()                                                            
s = ''                                                              
for i in n:                                                         
        if i==' ':                                                  
                                                                    
           s2.add(s)                                                
           s=''                                                     
                                                                    
        else:                                                       
            s += i                                                  
                                                                    
                                                                    
s2.add(s)                                                           
print()                                                             
lst=list(s2)                                                        
lst.sort()                                                          
for i in lst:                                                       
    print(i,end=' ' )                                               
