class IOstring():
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input()
    
    def printString(self):
        print(self.text.upper())
    

var = IOstring()
var.getString()
var.printString()