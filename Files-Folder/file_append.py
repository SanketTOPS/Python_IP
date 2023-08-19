fl=open('myfile.txt','a')

n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a Name:")

    fl.write(f"ID:{id}\n")
    fl.write(f"Name:{name}\n")