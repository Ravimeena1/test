class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width = width

    def Area_cal(self):
        area=self.width*self.length
        return area
obj=Rectangle(5,25)
print(obj.Area_cal())
