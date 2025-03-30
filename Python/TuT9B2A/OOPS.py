# Solving a problem by creating object is one of the most popular approaches in programming. This is called object-oriented Programming

# This content focuses on using reusable code (DRY Principle)
# [D]o-Not [R]epeat [Y]ourself 




# CLASS

# It is a blueprint for creating an object.



# OBJECT

# Is an instantiation of a class. when class is defined a template (info) is defined 
# Memory is allocated only after object instantiation
# 
# Objects of a given class can invoke the methods available to it without revealing the implementation
#  detailed the user - Abstractions & Encapsulation




# class employee:
#     language = "Py" # " This is a class attribute"
#     salary = 12000000000



# jerry = employee()
# jerry.name = "Jerry" # " This is an object attribute"
# print(jerry.language, jerry.salary, jerry.name)





# we identify the following in our problem 
# Noun -> Class -> Employee
# Adjective -> Attributes -> name,age,salary
# Verbs -> Methods -> getsalary(), increment()







# Class Attributes

# an Attribute that belongs to the class rather than a particular object






# rohan = employee()
# rohan.name = "Rohan"
# print(rohan.salary, rohan.language, rohan.name)



# Here name is Instance attribute also object attribute and salary and language are class
# attribute as they directly belong to the class









# Instance Attribute vs Class Attribute



# instance take priority or prefference over class attribute during assignment & and retrieval












# Self Parameter

class employee:
    language = "Py" # " This is a class attribute"
    salary = 12000000000

    # Required to use self whether we use it or not
    def getInfo(self):
        print(f"The Language is {self.language}. The salary is {self.salary}")
    
    def __init__(self): # Automatically calls itself = Dundar method, when object is created
        print("I will call Myself")
    
    def greet(self):
        print("Good Morning")
    

jerry = employee()
# jerry.name = "Jerry" # " This is an object attribute"
# print(jerry.language, jerry.salary, jerry.name)


jerry.greet()
jerry.getInfo()
# this above converts to employee.getInfo(jerry)















# Static Method

# Means that we do not need self for this as self is for descriptive 

# @staticmethod
# def greet():
#     print("Morning!")









# _INIT_()CONSTRUCTOR

# is a special method which is forst run as soon as the object is created

# _init_() is also known as constructor


# It takes self argument and can also take furthur arguments

# class Emp:
#     def __init__(self, name, salary, language):
#         self.name=name
#         self.salary=salary
#         self.language=language
#     def getSalary(self):
#         ...

# jerry = Emp("Jerry", 120000000, "Python")
# print(jerry.name, jerry.salary, jerry.language)







