class Rectangle:
    def __init__(self,x,y,width,height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return f'Rectangle : (x = {self.__x}, y = {self.__y}, w = {self.__width}, h = {self.__height}), 면적 = {self.__width*self.__height}'

r1 = Rectangle(0,0,100,100)
r2 = Rectangle(0,-10,10,10)
r3 = Rectangle(-100,0,120,100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)
