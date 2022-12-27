def re_function (x):
    newlist=[]
    for i in range(len(x)):
        temp=x.pop()
        ans=newlist.append(temp)
    return newlist

number =[1,2,3,4]
print(re_function(number))


def re_word(y):
    newWord=[]
    for j in range(len(y)):
        opp=y.pop()
        word=newWord.append(opp)
    return newWord

word =['cat','dog','snake','ant']
print(re_function(word))


