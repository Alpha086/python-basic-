def re_function(x):
    odd=[]
    even=[]
    for i in x:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    total =[odd,even]

    return total

newlist=[1,2,3,4,5,6,7,8,9]
print(re_function(newlist))