class sclass:
    def getString(self):
        self.text = input()
    
    def printString(self):
        print(self.text.upper())


obj = sclass()
obj.getString()
obj.printString()
