# Walrus Operator(Python 3.8):-
# :=
# if (n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements expected <= 3)")


# Output: List is too long (5 elements, expected <= 3)




# Types Definations
 # Type Hints are added using the Colon (:) syntax for variables and the  -> Syntax for function return Types.


# Variable type
# age: int = 25

# Function type
# def greeting(name: str) -> str:
#      return f"Hello, {name}!"





# Advanced Type Hints:

# Pythons typing module provides more advanced type hints, such as List, Tuples, Dict, and Union

# We can import List, Tuples, Dict types from the typing module like this:

# from typing import List, Tuple, Dict, Union

# # List Of Integers:
# numbers: List[int] = [1, 2, 3, 4, 5]

# # Tuple of a string and an Integer:
# Person: Tuple[str, int] = ("Alice", 30)

# # Dictionary with string keys and integer values:
# scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# # Union type for variables that can hold multiple types:
# identifier1: Union[int, str] = "ID123"
# identifier2 = 1234 # Also Valid

# print(numbers, Person, scores, identifier1)





# These annotations help in making the code self-documenting and allows developers to understand the data structures used at a glance.












# Match Case:

# Introduced in Python 3.10 introduced the match statement, which is similar to the switch statement found in other programming languages.

# The Basic syntax of the match statement involves matching a variable against several cases using the case keyword.

# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "NOT FOUND"
#         case 500:
#             return "INTERNAL SERVER ERROR"
#         case _:
#             return "UNKNOWN STATUS"
        

# # Usage
# print(http_status(200))
# print(http_status(404))
# print(http_status(500))
# print(http_status(403))






# Exception Handling in Python:

# Many built in exception are raised in python when something goes wrong.

# Exception in python can be handled using a try statement. the code that handles the exception is written in the except clause.
 
# a = int(input("Enter a Number: "))
# print(a)
 # with Running this code and typing any word or letter gives an error which looks bad as it shows that a code is crashed instead we should handle it with delicacy like below

# try:
#     a = int(input("Enter a number: "))
#     print(a)

# except Exception as e:
#     print(e)


# Specific Error Handling:

# Raising Exception:

# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))

# if(b == 0):
#     raise ZeroDivisionError("Hey Program Doesn't meant to divide numbers by Zero")
# else:
#     print(f"The Division a/b is {a/b}")








# TRY ELSE:

# if in try the code runs perfectly as user provides no error it runs else code

# try:
#     a = int(input("Enter a Number: "))
#     print(a)

# except Exception as e:
#     print(e)


# else:
#     print("I am inside else")






# TRY FINALLY:

# it gives finally clause which ensures execution of a piece of code inspective of the exception
# it runs in either of possible wys if runs successfully or in case of exception.

# try:
#     a = int(input("Enter a Number: "))
#     print(a)

# except Exception as e:
#     print(e)

# finally:
#     print("Hey I am inside of finally")



# Finally is best used in Function Modules:
# Like below:

# def main():
#     try:
#         a = int(input("Enter a Number: "))
#         print(a)

#     except Exception as e:
#      print(e)

#     finally:
#      print("Hey I am inside of finally")

# main()









# IF __NAME__ == '__MAIN__' in python

# __name__ evaluates to the name of the module in python from where the program is ran.

# if the module is being run directly from the command line, the '__name__' is set to string "__main__" thus this behavious is used to check whether the module is run directly or imported to another file.


# from mod import Func 







# Global Keyword:

# here a is a global keyword can be used anywhere and a in fun() is local keyword
# if we print a and then fun() the global keyword will be same but if fun() is first then the value will be changed as per to the local keyword

# a = 89


# def fun():
#     a = 3
#     print(a)


# fun()
# print(a)






# Enumerate Function in python:- 

# This function adds counter to an iterable and returns it.


# l = [3, 44, 653, 66]

# index = 0
# for item in l:
#     print(f"The item number {index} is {item}")
#     index += 1


# if We do it with Enumerate then it will be as follows:


# for index, item in enumerate(l):
#     print(f"The item number at index {index} is {item}")








# List Comprehension:
# is an elegant way to create lists based on existing lists:


# list1 = [1, 44, 64, 32]
# list2 = [2, 43, 55, 3]

# squaredList1 = []
# squaredList2 = []

# for item in list1:
#     squaredList1.append(item*item)
# for item in list2:
#     squaredList2.append(item*item)
# print(squaredList1)
# print(squaredList2)



# using Comprehension:

# squaredList1 = [i*i for i in list1]
# print(squaredList1)