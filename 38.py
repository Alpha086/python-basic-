name =input("enter yor name : ")
temp_var =""
i=0
while i<len(name):
    if name[i] in temp_var:
        temp_var += name[i]
    print (f"# {name[i]} : {name.count(name[i])}")
    i+=1