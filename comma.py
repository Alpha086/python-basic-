first_name,last_name=input("use comma between first name and last name : ").split(",")
print (f"length of your name is : {len(first_name)+len(last_name)}")
print (f"your count chart is : {first_name.count('a')+last_name.count('a')}")
name="nayeemd    is good boy and he is dreamer"
print(name.replace("d"," "))
is_pos1=name.find('is')
is_pos2=name.find("is",is_pos1+1)
print (f"second is position is : {is_pos2}")
print ('{first_name+last_name.replace("," ")}')