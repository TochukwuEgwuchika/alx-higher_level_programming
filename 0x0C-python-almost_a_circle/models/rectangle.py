#!/usr/bin/python3
"""
Contains the class Rectangle
"""
from base import Base

class Rectangle(Base):
    """Rectangle class that inherites from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_num):
        if type(x_num) is not int:
            raise TypeError("x must be an integer")
        if x_num < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_num

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_num):
        if type(y_num) is not int:
            raise TypeError("y must be an integer")
        if y_num < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_num

    def area(self):
        """Returns area of rectsngle instance"""
        return self.width * self.height

    def display(self):
        print("\n" * self.y)
        for i in range(self.height):
            print(" "*self.x, "#" * self.width, sep="")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                return
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
    
    def to_dictionary(self):
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
