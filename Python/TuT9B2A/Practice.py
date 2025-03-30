# from random import randint

# Q1 = Create a Prgrammmer Class for storing information of few programmers working at microsoft

# class Programmer:
#     company = "Microsoft"
#     #as every member of this class is working in microsoft Class Attribute
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin
#     print("\nBelow Works in Microsoft.......\n")
    

# p = Programmer("Jerry", 120000000, 302017)
# print(f" {p.name},\n {p.salary},\n {p.pin}\n")

# r = Programmer("GunGun", 130000000, 302017)
# print(f" {r.name},\n {r.salary},\n {r.pin}\n")

# s = Programmer("Samyak", 140000000, 302017)
# print(f" {s.name},\n {s.salary},\n {s.pin}\n")









# Q2 = class Calculator capable of finding square, cube and ,square root of a number



# class Calculator:
    
#     def __init__(self, n):
#         self.n = n
    
#     def square(self):
#         print(f"The Square of {self.n} is:\n{self.n*self.n}")

#     def cube(self):
#         print(f"The Cube of {self.n} is:\n{self.n*self.n*self.n}")

#     def squareroot(self):
#         print(f"The SquareRoot of {self.n} is:\n{self.n**1/2}")

# a = Calculator(4)

# a.square()
# a.cube()
# a.squareroot()











# Q3 = Create a Class with a class attribute a; create an object from it and set 'a'
# directly using object.a = 0 Does this change the class attribute




# class Demo:
#     a = 4

# o = Demo()
# print(o.a) # Class Attribute as instance not yet present

# o.a = 0 # Instance Attribute is set
# print(o.a) # Prints instance attribute because it is now present


# No = As Class Attribute isn't changed but instance Attribute is been setted up












# Q4 = Add a Static method n problem 2 to greet the user with hello



# class Calculator:
    
#     def __init__(self, n):
#         self.n = n
    
#     def square(self):
#         print(f"The Square of {self.n} is:\n{self.n*self.n}")

#     def cube(self):
#         print(f"The Cube of {self.n} is:\n{self.n*self.n*self.n}")

#     def squareroot(self):
#         print(f"The SquareRoot of {self.n} is:\n{self.n**1/2}")


#     @staticmethod
#     def hello():
#         print(f"Hello There!")

# a = Calculator(4)
# a.hello()
# a.square()
# a.cube()
# a.squareroot()













# Q5 = Class train which has methods to book a ticket get status (no of seats)
# and get fare information of train running under indian railways


# class Train:
#     def __init__(self):
#         # Initialize Attributes to None Initially
#         self.name = None
#         self.number = None
#         self.whereto = None
#         self.fromwhere = None
#         self.trainNo = None
#         # self.trainNo = None
#         # self.fromwhere = None
#         # self.whereto = None

#     def book(self):
#         print("To Book the ticket, Press Yes or No for Cancellation..................\n")
#         b = input("Enter Your Choice (YES or No):\n").lower() # For Input of lowercase
#         if b == "yes":
#             print("Provide further details For bookinf:\n")
#             self.name = input("Enter Your Name: \n")
#             self.number = input("Enter Your Number: \n")
#             self.fromwhere = input("Enter Your Departure Details: \n")
#             self.whereto = input("Enter Your Destination: \n")
            


#             print("\nLoading Ticket Details.....................\n")
#             print("Confirm Below Details:\n")
#             print(f"Name: {self.name}\nNumber: {self.number}\nFrom: {self.fromwhere}\nDestination: {self.whereto}\n")
            
#             c = input("Confirm (Yes or No):").lower()
#             if c == "yes":
#                 print("Confirming Booking...............")
#                 print("\n::::::::::::::Enter Further Details::::::::::::::\n")
                
#             else:
#                 print("Try Again From start:\n")
#         elif b == "No" or b == "no":
#             print("\nThank You. You May Move Forward. ")

#         else:
#             print("\nOnly Expected Anwers will Be Entertained. ")
    
    
#     def getStatus(self):
#         self.trainNo = randint(12000, 13000)
#         print(f"The Train No: {self.trainNo} is running on Time")


#     def getFare(self):
#         print(f"The Ticket Fare in Train no: {self.trainNo} from {self.fromwhere} to {self.whereto} is {randint(250, 1500)}")
#         print("\n::::::::::::::Printing Ticket::::::::::::::\n")




# train = Train()
# train.book()
# train.getStatus()
# train.getFare()










# Q6 = Program 


# Inheritence and More On OOPS


# Q1 = Create a class (2-D vector) and use it to create another class representing a 3-D vector.

# class TwoDector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"the Vector as {self.i}i + {self.j}j")

# class ThreeDVector(TwoDector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k
#     def show(self):
#         print(f"the Vector as {self.i}i + {self.j}j + {self.k}k")



# o = TwoDector(1, 2)
# o.show()
# b = ThreeDVector(1, 2, 3)
# b.show()




# Q2 = Create a class 'Pets' from a class 'Animal' and further create a class 'Dog' from 'Pets' Add a method 'bark' to class 'Dog'


# class Animals:
#     pass

# class Pets(Animals):
#     pass

# class Dog(Pets):

#     @staticmethod
#     def bark():
#         print("Bow Bow!")
    


# d = Dog()
# d.bark()






# Q3 = Create a class 'Employee' and add salary and increment properties to it.

# class Employee:
#     salary = 50
#     increment = 10


# e = Employee()
# e.salary = 50
# e.increment = 10

# if we want to add them a class property we will add them under class Employee but if instance propertty we will add


# Q3 Conitnuattion = Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary



# class Employee:
#     salary = 50000
#     increment = 10
    
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * self.increment/100)

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment = (salary/self.salary - 1) * 100


# e = Employee()

# e.salaryAfterIncrement = 55000
# print(e.increment)

# print(e.salaryAfterIncrement)






# Q4 = Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)

#     def __str__(self):
#         return f"{self.r}r + {self.i}i"


# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2)


# Learn Complex Numbers





# Q5 = Write a class vector representing a vector of n dimensions, Overload the + and * operator which calculates the sum and dott(.) product of them

# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result

#     def __mul__(self, other):
#         result = self.x * other.x, self.y * other.y, self.z * other.z
#         return result
    
#     def __str__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"




# # Test the implementation
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)  # Same dimension Vector

# print(v1 + v2) # output: Vector (5, 7, 9)
# print(v1 * v2) # output: (4, 10, 18): 32

# print(v1 + v3) # Output: Vector(8, 10, 12)
# print(v1 * v3) # Output: (7, 16, 27): 50









# Q6 = Write a __str__ method to print the vector as follows:
#      7i + 8j + 10k




# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result

#     def __mul__(self, other):
#         result = self.x * other.x, self.y * other.y, self.z * other.z
#         return result
    
#     def __str__(self):
#         return f"Vector({self.x}i + {self.y}j + {self.z}k)"




# # Test the implementation
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)  # Same dimension Vector

# print(v1 + v2) # output: Vector (5, 7, 9)
# print(v1 * v2) # output: (4, 10, 18): 32

# print(v1 + v3) # Output: Vector(8, 10, 12)
# print(v1 * v3) # Output: (7, 16, 27): 50)






# Q7 = Override the __len__() method in vector of problem 5 to display thre dimension of the vector

# class Vector:
#     def __init__(self, l):
#         self.l = l

 
#     def __len__(self):
#         return len(self.l)



# # Test the implementation
# v1 = Vector([1, 2, 3])
# print(len(v1))






