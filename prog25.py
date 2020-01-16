class Mobile:
    def __init__(self,price,color,brand):
        self.price=price
        self.color=color
        self.brand=brand
    def show(self):
        print(self.price)
        print(self.color+"\n"+self.brand)


obj=Mobile(50000,'silver','i5')
obj.show()
