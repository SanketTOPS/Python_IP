def myfunc():
    print("This is my function.")


def getsum(a,b):
    print("Sum:",a+b)


def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)


# Calling a function
myfunc()
getsum(23,45) #static param

stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")
getdata(stid,stnm,stsub) #dynamic
