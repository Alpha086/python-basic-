def common(x,y):
    add=[]
    for i in x:
        if i in y:
            add.append(i)
    return add

list1=[1,2,3,4]
list2=[1,2,6,7]
print(common(list1,list2))
