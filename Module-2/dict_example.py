stdata={}

keys=['id','name','sub','city']

for i in range(len(keys)):
    value=input(f"Entyer a value of {keys[i]}:")

    stdata[keys[i]]=value

print(stdata)
#{id:101,name:'sanket'}