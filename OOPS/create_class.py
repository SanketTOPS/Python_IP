class student:
    def __init__(self) -> None:
        print("This is OOP!")
    

    stid=12
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)


# Object
st=student()
st.getdata()