import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("(", self.x, ",", self.y, ")")
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point(0, 0)
p2 = Point(3, 4)
p1.show()  # ( 0 , 0 )
p2.show()  # ( 3 , 4 )
print(p1.dist(p2))  # 5.0
p1.move(1, 1)
p1.show()  # ( 1 , 1 )
