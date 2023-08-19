"""fl=open('hello.txt','w')

fl.write('Good Morning!')"""


# File write using user input

id=input("Enter an ID:")
name=input("Enter a Name:")

fl=open('myfile.txt','w')

fl.write(id)
fl.write(name)


