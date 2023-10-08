#热爱学习的CXQ
import math

class Point:

    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
        print("创建了Point(%d,%d,%d)" %(self.x,self.y,self.z))

    def __str__(self):
        return "Point(%d,%d,%d)" %(self.x,self.y,self.z)

    def __add__(self, other):
        if isinstance(other,Point):
            raise TypeError("点和点不能相加")
        if isinstance(other,Vector):
            return Point(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self, other):
        if isinstance(other,Point):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        if isinstance(other,Vector):
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)

    def __eq__(self, other):
        if self.x==other.x and self.y==other.y and self.z ==other.z:
            return True
        else:
            return False

    def __lt__(self, other):
        modself=math.sqrt(self.x**2+self.y**2+self.z**2)
        modoth=math.sqrt(other.x**2+other.y**2+other.z**2)
        if modself<modoth:
            return True
        else:
            return False

class Vector:

    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
        print("创建了Vector(%d,%d,%d)" %(self.x,self.y,self.z))

    def __str__(self):
        return "Vector(%d,%d,%d)" %(self.x,self.y,self.z)

    def __add__(self, other):
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y,self.z+other.z)
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self, other):
        if isinstance(other,Point):
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)
        if isinstance(other,Vector):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)

    def __eq__(self, other):
        if self.x==other.x and self.y==other.y and self.z ==other.z:
            return True
        else:
            return False

    def __lt__(self, other):
        modself=math.sqrt(self.x**2+self.y**2+self.z**2)
        modoth=math.sqrt(other.x**2+other.y**2+other.z**2)
        if modself<modoth:
            return True
        else:
            return False

    def __mul__(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        new_x = self.x * math.cos(angle_radians) - self.y * math.sin(angle_radians)
        new_y = self.x * math.sin(angle_radians) + self.y * math.cos(angle_radians)
        return Vector(new_x, new_y, self.z)

    def __truediv__(self, angle_degrees):
        return self.__mul__(-angle_degrees)

point1 = Point(1, 2, 3)
point2 = Point(4, 5, 6)
vector = Vector(2, 3, 4)

print(point1 + vector)
print(point2 - point1)
print(point1 == point2)
print(vector * 45)  # 逆时针旋转45度
print(vector / 30)  # 顺时针旋转30度