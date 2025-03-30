# Snake water Gun game
import random

'''
1 = snake
-1 = water
0 = gun
'''
computer = random.choice([-1, 0, 1])
you = input("Enter Your Choice (s/w/g): \n")

youDic = {"s": 1, "w": -1, "g": 0}
reverseDic = {1: "Snake", -1: "Water", 0: "Gun"}

younum = youDic[you]

# REverse Dic alowos changes or updates without changing anything in previous data
print(f"You Choose {reverseDic[younum]} \nComputer Choose {reverseDic[computer]}")

# if(computer == younum):
#     print("DRAWW")


# else:
#     if(computer  == -1 and younum == 1):
#         print("You Win")
    
#     elif(computer == -1 and younum == 0):
#         print("You Loose")

#     elif(computer == 1 and younum == -1):
#         print("You loose")

#     elif(computer == -1 and younum == 0):
#         print("You Won")

#     elif(computer == 0 and younum == -1):
#         print("You won ")

#     elif(computer == 0 and younum == 1):
#         print("You losse")

#     else:
#         print("Try Right Choice")



# Better Code: (Shorter):


if((computer - younum) == -1 or (computer - younum) == 2):
        print("You Loose")
elif(computer == younum):
        print("DRAWW")
else:
        print("You Win")
        