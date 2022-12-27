import random
winning_num=random.randint(1,100)
guess=1
number= int(input("enter yor number 1 to 100 : "))
end_game=False

while not end_game:
    if number==winning_num:
      print (f"you win,and you tried {guess} time")
      end_game=True
    else:
        if number < winning_num:
            print("too low")
            guess+=1
            number= int (input("try again : "))
        else:
            print("too high")
            guess+=1
            number=int (input("try again : "))