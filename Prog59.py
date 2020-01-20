class Person:                                
                                             
    def set_gender(self,gender):             
        self.gender=gender                   
                                             
class Male(Person):                          
    def get_GetGender(self):                 
        print(self.gender)                   
                                             
class Female(Person):                        
    def get_GetGender(self):                 
        print(self.gender)                   
obj=Male()                                   
obj.set_gender("male")                       
obj.get_GetGender()                          
obj1=Female()                                
obj.set_gender("Female")                     
obj.get_GetGender()                          
