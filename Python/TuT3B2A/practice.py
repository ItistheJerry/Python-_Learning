# Q1 = Program to store seven fruits in a list entered by the user

# Fruits = []

# f1 = input("Enter Fruit name: ")
# Fruits.append(f1)

# f2 = input("Enter Fruit name: ")
# Fruits.append(f2)

# f3 = input("Enter Fruit name: ")
# Fruits.append(f3)

# f4 = input("Enter Fruit name: ")
# Fruits.append(f4)

# f5 = input("Enter Fruit name: ")
# Fruits.append(f5)

# f6 = input("Enter Fruit name: ")
# Fruits.append(f6)

# f7 = input("Enter Fruit name: ")
# Fruits.append(f7)


# print(Fruits)






# Q2 = Program to Accept marks of 6 students and display them in a sorted manner
# Marks = []

# s1 = int(input("Enter Marks of student1: ")
# Marks.append(s1)

# s2 = int(input("Enter Marks of student2: ")
# Marks.append(s2)

# s3 = int(input("Enter Marks of student3: ")
# Marks.append(s3)

# s4 = int(input("Enter Marks of student4: ")
# Marks.append(s4)

# s5 = int(input("Enter Marks of student5: ")
# Marks.append(s5)

# s6 = int(input("Enter Marks of student6: ")
# Marks.append(s6)

# print("Printing Marks")
# print(Marks)

# print("Sorting Marks")
# Marks.sort()
# print(Marks)



# # Initialize an empty list to store the marks
# Marks = []

# # Take marks input from the user for 6 students
# for i in range(1, 7):
#     while True:
#         try:
#             mark = int(input(f"Enter Marks of student{i}: "))
#             if 0 <= mark <= 100:
#                 Marks.append(mark)
#                 break
#             else:
#                 print("Please enter marks between 0 and 100.")
#         except ValueError:
#             print("Invalid input! Please enter an integer.")

# # Print the original marks
# print("\nOriginal Marks:")
# print(Marks)

# while True:
#     # Ask if the user wants to sort the list
#     Q1 = input("\nWould you like to sort the list for you? (Yes/No): ").strip().lower()

#     if Q1 == 'yes':
#         Marks = sorted(Marks)  # Sort the list and update Marks
#         print("\nPrinting Sorted Result:")
#         print(Marks)
#         break  # Exit the loop after sorting
#     elif Q1 == "no":
#         print("\nPrinting Original Marks:")
#         print(Marks)
#         break  # Exit the loop if the user doesn't want to sort
#     else:
#         # If the input is invalid, ask again
#         print("Invalid input. Please enter 'Yes' or 'No'.")






# Q3 = Program to check that a  tuple type cannot be changed in python


# a = (34, 54, "Jerry")

# a[2] = "Larry"
# = Result is that a tuple type cannot be changed




# Q4 = Program to sum a list with 4 numbers

# Numb = [34,43,65,77]

# print(sum(Numb))




# Q5 = Program to count the number of zeroes in the following

# a =(7, 0, 8, 0, 0, 9)

# n = a.count(0)
# print(n)