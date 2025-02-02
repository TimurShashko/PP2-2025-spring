class dialog:
    def __init__(self):
        self.name = ""
    def getString(self):
        print("What's your name?")
        self.name = input()
    
    def printString(self):
        print(self.name.upper(), ", nice to meet you!")

you = dialog()
you.getString()
you.printString()