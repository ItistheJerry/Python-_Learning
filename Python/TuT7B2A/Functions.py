# Is a Group of statements performing a specific task
# When a program get bigger in size and its complexity grows it gets difficult for a program to keep track on which piece of code is doing what
# A function can be reused by the programmer in a given program any number of time.

# Syntax:
# 
# 
# def func()
# 
# 
# # Examle = Average of 4 numbers

# a = 12
# b = 34
# c = 54
# d = 43

# average = (a + b + c + d)/4

# print(average)


# Now if i need to use this code again and again in every 20 lines I can't write the code again and again. so we create a function


# def avg():
#     a = int(input("Enter Number: \n"))
#     b = int(input("Enter Number: \n"))
#     c = int(input("Enter Number: \n"))
#     d = int(input("Enter Number: \n"))


#     average = (a + b + c + d)/4
#     print(average)





# avg() # Calling the Function to perform code










# Function Definition 
# The Part Containing the exact set of instructions which are excecuted during the function call



# Q = Program to greet a user with Good Day using Function



# def gm():
#     user = input("Enter Name User: \n")
#     print(f"Good Morning {user} ")

# above is Function Definition


# Below is Function Call
# gm()














# Types = 
# Two Types
# Built In Functions (Already Present in Python Languages in libraries and framwork) print() len() range()
# User Defined Functions (Defined and Created By User)





# Function Arguments 

# A Function can accept some value it can work with. We can Put these values in the parentheses


# def greet(name, ending):
#     gr = "Heylo " + name
#     print(ending)
#     return gr

# def greet(name):
#     print("Good Day, " + name)
#     return "Have a Nice Day!"



# a = input("Enter Your Name: \n")
# print(greet(a), end="")



# a = greet("Jerry", "Thank You")
# print(a)



# a = input("Enter Your Name: \n")
# print(greet(a))



# a = greet(input("Enter Your Name: \n"))
# print(a)







# Default Parameter Value

# def goodDay(name, ending="Thank You"):
#     print(f"Good Day, {name}")
#     print(ending)

# Here if we don't provide a data for ending variable of the above function it is set to provide a specific data to be printedf
# If we do provide data it will print it than as the updated data.


# goodDay("Jerry", "Broo")

