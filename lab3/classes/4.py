class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print("(", self.x, ";", self.y, ")")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return (((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5)

p1 = point(3, 4)
p2 = point(6, 8)
p1.show() 
p2.show()  
print("Distance:", p1.dist(p2))  
p1.move(10, 12)
p1.show()  