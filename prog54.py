class Shape:
   def Area_cal(self):
       return print("0")
   class Square:
       def __init__(self,length):
           self.length=length
       def Area_cal(self):
           return print(self.length*self.length)
  # obj=Square(self.length)

obj=Shape()
obj1=Shape.Square(5)
obj.Area_cal()
obj1.Area_cal()
