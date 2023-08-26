class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("enter number of cars:")
        self.bal=input("enter bank balance:")

class son(father):
    def printdata(self):
        print("Car:",self.car)
        print("Bank Balance:",self.bal)


sn=son()
sn.getdata()
sn.printdata()