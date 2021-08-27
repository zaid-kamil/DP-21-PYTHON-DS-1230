# super class
class Shape:

    color = 'white' # class variable

    def __init__(self, height,width):
        '''
        the general contructor of the class,
        takes the height and width of the shape
        '''
        self.height = height # instance variable
        self.width = width # instance variable

    def area(self):
        '''
        calculates the area of the shape
        '''
        return self.height * self.width

class Rectangle(Shape):
    '''
    subclass of the class Shape
    '''
    
class Triangle(Shape):  
    # override the area method - method overriding
    def area(self):
        '''
        calculate the area of the triangle
        '''
        return (self.height * self.width) / 2


class Circle(Shape):
    
    # override the constructor - constructor overriding
    def __init__(self, radius):
        self.radius = radius # instance variable
        super().__init__(radius, radius) # call the constructor of the super class
        
    # override the area method - method overriding
    def area(self):
        return 3.14 * self.radius * 2
    
obj = Rectangle(10,20)
print(obj.area())
print(obj.color)

ob2 = Triangle(10,20)
print(ob2.area())

ob3 = Circle(10)
print(ob3.area())



