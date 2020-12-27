class Circle:
    PI = 3.14
    def __init__(self,x,y,radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def set_x(self,x):
        self.__x = x
    def set_y(self,y):
        self.__y = y
    def set_radius(self,radius):
        self.__radius = radius

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_radius(self):
        return self.__radius

    def area(self):
        return Circle.PI * self.__radius**2

    def overlaps(self,c):
        A1 = ((self.__x - c.__x)**2 + (self.__y - c.__y)**2)**0.5
        B1 = self.__radius + c.__radius
        if A1 <= B1:
            return True
        else:
            return False

    def contains(self, c):
        A2 = ((self.__x - c.__x) ** 2 + (self.__y - c.__y) ** 2) ** 0.5
        B2 = self.__radius - c.__radius
        if A2 <= B2:
            return True
        else:
            return False

    def __repr__(self):
        return f'Circle : (x = {self.__x}, y = {self.__y}, radius = {self.__radius}), 면적 = {self.area()}'

c1 = Circle(0,0,100)
c2 = Circle(0,-10,10)
c3 = Circle(-100,0,120)

print('c1 = ',c1)
print('c2 = ',c2)
print('c3 = ',c3)

print('c1 contains c2 :', c1.contains(c2))
print('c1 contains c3 :', c1.contains(c3))
print('c1 overlaps c2 :', c1.overlaps(c2))
print('c1 overlaps c3 :', c1.overlaps(c3))