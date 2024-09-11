class InputOutString():
    def __init__(self):
        self.s = ""
 
    def getString(self):
        print('输入字符串：')
        self.s = input()
 
    def printString(self):
        print (self.s.upper())
 
 strObj = InputOutString()
 strObj.getString()
 strObj.printString()
