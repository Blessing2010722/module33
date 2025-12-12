class squre:
    def__init__(self, side):
        self.side = side
    def area(self):
        print("my area is : ",self.side**2")

class circle:
    def__init__(self,radius):
        self.radius = radius
    def area(self):
        print("my area is : ",3.1416*self.raduis")
mysqure = squre(5)
myraduis = circle(5)

fo shape in (mysqure,myraduis):
   shape.area()