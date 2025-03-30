#  Q1 = Create two virtual environments install few packages in the first one, how do you create a similar environment in the second one.




# Q2 = Write a program to input name, marks and phone number of a student and format it using the format function like below:
# The name of the student is Jerry his marks are 72 and phone number is 9987787887

# Detail = "The World is Lacking Students Like {} His Marks were {} in overall Exams but if you want to schedule a meeting call his assistant at the Phone number {}".format("Jerry", 99, 9899788293)
# print(Detail)


# Q3 = A list Contains the multiplication table of 7. Write a program to Convert it to Vertical String Of same Numbers

# num = int(input("Enter the Number: "))
# table = [str(num*i) for i in range(1, 11)]

# s = "\n".join(table)
# print(s)







# Q4 = Write a program to filter a list of numbers which are divisible by 5.

# l = [2, 4, 65, 67, 90, 101, 205, 300, 199, 23453, 4432, 445090, 3333432325]


# def div(n):
#     if(n % 5 == 0):
#         return True
#     return False

# div5 = filter(div, l)
# print(list(div5))






# Q5 = Write a Program to find the maximum of the numbers in a list using the reduce function

# from functools import reduce

# l = [2, 4, 65, 67, 90, 101, 205, 300, 199, 23453, 4432, 445090, 3333432325]

# def great(a, b):
#     if(a>b):
#         return a
#     return b

# print(reduce(great, l))






# Q6 = Run pip freeze for the system interpreter. Take the Contents and create a similar virtualenv




# Q7 = Explore Flask Modeule and create a web server using Flask and Python


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# for further see app.py