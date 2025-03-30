# Q1 = Program using functions to find the greatest of three numbers
# def great(a, b, c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
#     else:
#         return "Try Again!!..."
    





# a = int(input("Enter Number 1: \n"))
# b = int(input("Enter Number 2: \n"))
# c = int(input("Enter Number 3: \n"))



# print(f"The Greatest Number among all of the above is: {(great(a,b,c))}")








# Q2 = Program using function to convert celsius to fahrenheit

# def temp_chanage(cel_temp):
#     far = cel_temp * 9/5 + 32
#     return far





# cel_temp = int(input("ENTER A TEMP IN CELSIUS: \n"))


# print(f"The Temprature change from celsius to fahrenheit is: {(temp_chanage(cel_temp))}")














# Q3 = How to Prevent a python print() function to print a new line at the end

# a=1
# b=3
# c=5


# print("a")
# print("b", end="")
# print("c", end="")










# Q4 = A Recursive function to calculate the sum of the first n natural numbers

# natural = int(input("Enter the number till you want the sum of: \n"))

# def sum(n):
#     if(n == 1):
#         return 1
#     return sum(n-1) + n


# n = int(input("Enter the Number You want the sum till: \n"))
# print(f"The sum of the First natural n numbers is: {(sum(n))}")











# Q5 = Python Function For 

# ***
# **
# *

# for n = 3

# def pattern(n):
#     if(n == 0):
#         return
#     print("*" * n)
#     pattern(n-1)




# n = int(input("Enter Number of stars You Want: \n"))
# print(f"The stars are Below \n {(pattern(n))}")








# Q6 = Program Function that Converts Inches to cms

# def conversion(inch):
#     cms = inch * 2.54
#     return cms






# inch = int(input("Enter The Inches To Be Convreted: \n"))
# print(f"The Converted CMS is: {(conversion(inch))}")











# Q7 = Program Function to remove a given word from a list ad strip it at the same time

# def rem(k, word):
#     n = []
#     for item in k:
#         if not(item == word):
#             n.append(item.strip(word))

#     return n
# if the item == word true then we will add the word to n and strip the word from word in the item 





# k = ["Jerry", "God", "Berry"]


# print(rem(k, "ry"))










# Q8 = Program function to print a table for a given number


# def table(numb):
#     print(f"Multiplication Table for {numb}:")
#     for i in range(1, 11):
#         print(f"{numb} x {i} = {numb * i}")
    
'''
Prints the multiplication table for the given number up to a specified range.
    
    :param number: The number for which the table is to be printed
    :param upto: The range up to which the table is printed (default is 10)
    """
'''






# numb = int(input("Enter the number You want table of: \n"))
# print(f"The Table is: {table(numb)}")