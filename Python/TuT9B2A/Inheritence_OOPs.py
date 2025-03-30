# Inheritence is a way of creating a new class from an existing class

# # Parent Class
# class Employee:
#     company = "ITC"
#     def show(self):
#         print(f"The Name of the Employee is {self.name} and the salary is {self.salary}")

# # Inherited or Child CLass
# class Programmer(Employee):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.Language} language")



# a = Employee()
# b = Programmer()

# print(a.company, b.company)






# Types of Inheritance
# 1. Single
# 2. Multiple
# 3. Multilevel



# SINGLE INHERITANCE
# OCCURS WHEN child class inherits only a single parent class 


# MULTIPLE INHERITANCE
# Occurs when the child class inherits from more than one parent classes


# # Parent Class
# class Employee:
#     company = "ITC"
#     name = "Default"
#     def show(self):
#         print(f"The Name of the Employee is {self.name} and the Company is {self.company}")


# class coder:
#     language = "Python"
#     def printLanguage(self):
#         print(f"Out of all the languages here The the language you are good at {self.language}")

# # Inherited or Child CLass with multiple Inheritance
# class Programmer(Employee, coder):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The Company name is {self.company} and he is good with {self.language} language")



# a = Employee()
# b = Programmer()

# b.show()
# b.printLanguage()
# b.showLanguage()






# MULTILEVEL INHERITANCE
# When a child class becomes a parent for another child class

# Like from Employee to Programer and Programmer to Program Manager



# class Employee:
#     a = 1

# class Programmer(Employee):
#     b = 2

# class Manager(Programmer):
#     c = 3



# o = Employee()
# print(o.a) # Prints the a attribute
# # print(o.b) # Shows an error as there is no b attribute in employee class

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)










# SUPER METHOD

# Super() method is used to access the methods of a super class in the derived class

# super().__init__()
# __init__() Calls constructor of thr base class

# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")
#     a = 1

# class Programmer(Employee):
#     def __init__(self):
#         print("Constructor of Programmer")
#     b = 2

# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of Manager")
#     c = 3



# o = Employee()
# print(o.a) # Prints the a attribute
# # print(o.b) # Shows an error as there is no b attribute in employee class

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)


# # If we want to run Manager and all the abover two Constructor as well










# CLASS METHOD
# Method is a method which is bound to the class and not the object of the class.
# @classmethod is used to create a class method

# @classmethod
#    def(cls,p1,p2):



# class Employee:
#     a = 1

#     def show(self):
#         print(f"The class value of a is {self.a}")

# e = Employee()
# e.a = 45 # Instance attribute

# e.show()


# If we need class attribute then 
# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The class value of a is {cls.a}")

# e = Employee()
# e.a = 45 # Instance attribute

# e.show()


# self means object on which method is running and cls on which method is running




# PROPERTY DECORATOR
# if e = Employee() is an object of class employee, we can print [e.name] to print the ename by intentionally calling name() function.

# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The class value of a is {cls.a}")
    
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name(self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# # .split gives "Jerry Jain" to ["Jerry", "Jain"] from the space(" ")
    

# e = Employee()
# e.a = 45 # Instance attribute


# e.name = "Jerry Jain"
# print(e.fname, e.lname)

# e.show()




 # Abstraction and Encapsulation
 # Abstraction = Implimenting details are hidden from user 
 # Encapsulation = Many working Components are packed together here class is one















 # OPERATOR OVERLOADING



# Operator in python can be overload using dunder methods.
# These methods are called when a given operator is used on the objects.
# Operators in python can be overloaded using the following methods.

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n 

n = Number(1)
m = Number(2)


print(n + m)




# TYPES OF
# p1+p2 = p1.__add__(p2)
# p1-p2 = p1.__sub__(p2)
# p1*p2 = p1.__mul__(p2)
# p1/p2 = p1.__truediv__(p2)
# p1//p2 = p1.__floordiv__(p2)

# __ __ methods are called dunder methods


# OTHER DUNDER/MAGIC methods in PYTHON:

# str__() used to set what gets displayed upon calling str(obj)


# __len__() used to set what gets displayed upon caling.__len__() or len(obj)


