class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("enter nirav's ID:")
        self.nsub=input("enter nirav's subject:")

class mitesh(nirav):
    mid=0
    msub=''

    def m_getdata(self):
        self.mid=input("enter mitesh's ID:")
        self.msub=input("enter mitesh's subject:")
    
class tops(mitesh):
    def printdata(self):
        print("--------Nirav's Info--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("--------Mitesh's Info--------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Subject:",self.msub)

tp=tops()
tp.n_getdata()
tp.m_getdata()
tp.printdata()