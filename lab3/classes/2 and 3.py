class shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area:", 0)

class square(shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print("Area:", self.length * self.length)

chtoto = shape()
chtoto.area()
kvadrat = square(5)
kvadrat.area()

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print("Area:", self.length * self.width)

pryamoug = rectangle(5,2)
pryamoug.area()