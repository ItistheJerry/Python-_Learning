# Q1 = Write a program to open three files 1.txt, 2.txt, 3.txt if any these files are not present a message without exiting program must be printed prompting the same.
# try:

#     with open("/Users/thejoker/Desktop/Python/TuT10B2A/1.txt", "r") as f:
#      print(f.read())

# except Exception as e:
#     print(e)

# try:   
#     with open("/Users/thejoker/Desktop/Python/TuT10B2A/2.txt", "r") as f:
#      print(f.read())

# except Exception as e:
#     print(e)

# try:
#     with open("3.txt", "r") as f:
#      print(f.read())

# except Exception as e:
#     print(e)



# print("Thank You")






# Q2 = Program to print third, fifth and seventh element from a list using enumerate func

# l = [1, 2, 4, 53, 55, 32, 432, 4234, 4432]

# for index, item in enumerate(l):
#     if index == 2 or index == 4 or index == 6:
#         print(f"The Element at index {index + 1} is {item}")






# Q3 = write a list comprehension to print a list which contains the multiplication table of a user entered number:

# num = int(input("Enter a number for its table: \n"))

# table = [num * i for i in range(1, 11)]
# print(table)





# Q4 = Write a program to display a/b where a and b are integers, if b = 0, display infinite by handing the 'ZeroDivisionError'

# a = int(input("Enter a Number1: \n"))
# b = int(input("Enter a Number2: \n"))

# if(b == 0):
#     raise ZeroDivisionError(" Hey You can have this for a treat!!")

# else:
#     print(f"The Division of a/b is: \n{a/b}")







# Q5 = Store the multiplication table generated in problen 3 in a file named tables.txt

# num = int(input("Enter a number for its table: \n"))

# table = [num * i for i in range(1, 11)]
# print(table)

# with open("/Users/thejoker/Desktop/Python/TuT10B2A/Tables.txt", "w") as f:
#     for value in table:
#      print(f.write(str(value) + "\n"))
     

# with open("/Users/thejoker/Desktop/Python/TuT10B2A/Tables.txt", "w") as f:
#      f.write(f"Table of {num}: {str(table)} \n")







