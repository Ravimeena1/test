class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area_cal(self):
        area=3.1416*self.radius*self.radius
        return area
obj=Circle(5)
print(obj.Area_cal())
