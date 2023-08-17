"""from topspkg import mylib,newlib

mylib.getdata(1,'Sanket')

newlib.getsum(23,54)
newlib.production(34,65)"""


from topspkg.genpkg import mylib
from topspkg.auth import myauth

mylib.getdata(1,'Sanket')
myauth.signup(1,'Sanket2020','test@123')
