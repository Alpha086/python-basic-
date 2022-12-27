def re_word(x):
    newlist=[]
    for i in x:
        newlist.append(i[::-1])
    return newlist
lists=['cow','crow','dog','python']
print(re_word(lists))