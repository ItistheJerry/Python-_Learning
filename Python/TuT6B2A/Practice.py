# Q1 = Program to print multiplication tabel of a given number using for loop inpython
# n = int(input("Enter the number you want table of: \n"))


# for i in range(1, 11):
    # f helps to use variables in string
    # print(f"{n} X {i} = {n * i}")




# for right angle pyramid
# n = (input("Enter the number you want table of: \n"))


# for i in range(1, 11):
    # f helps to use variables in string
    # print(f"{n} X {i} = {n * i}")






# Q2 = Write a program to greet all the person name stored in a list ("l") and which starts with S


# l = ["Jerry", "Samyak", "Sarthak", "Jhonny", "SexyMamba", "Zoravar"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")








# Q3 = Attemp Problem number 1 with while loop
# n = int(input("Enter the number you want table of: \n"))

# i = 1

# while(i<11):
#     print(f"{n} X {i} = {n * i}")
#     i += 1






# Q4 = Program to find whether a given number is prime or not


# for i in range(1, n+1): # If n is divisible by i # without any remainder. if n % i == 0: # Increment the counter. cnt = cnt + 1 # If the number of # factors is exactly 2 if cnt == 2: # Return True, indicating # that the number is prime. return True # If the number of # factors is not 2.
# n = int(input("Enter a number to check is Prime Nature:  \n"))

# for i in range(2, n):
#     if(n % i) == 0:
#         print("Number is not Prime")
#         break
#     else:
#         print("Yaaah Prime Number is")
#         break







# Q5 = A Program to find the sum of first n(User) natural numbers using while loop



# n = int(input("Enter the Number: \n"))
# i = 1
# sum = 0
# while(i<=n):
    # sum += i #Here the sum intitially being 0 adds value of i which is i and as below
    # i+=1 # i's value is incrementing with each loop end it goesback and updates value till it is equal to n
    # and adds into sum till it is equal to n

# print(sum)








# Q6 = Program to find factorial of given number using for loop
# Factorial is n! = n-5 * n-4 ........n
# n = int(input("Enter Number To find Factorial:  \n"))

# product = 1 # when multiplying start by 1 unlike addition where we can start with 0

# for i in range(1, n+1): # if only used n then it would have stopped at 4 as default is n-1 so we typed n+1 which ends at 5
    # product = product * i

# print(f"The Factorial of {n}! is {product}")








# Q7 = Program to make a traingle pattern (Important)

#      * = 2 spaces

#    * * * = 1 spaces

#  * * * * *  = 0 spaces for n = 3


# n = int(input("Enter Number:   \n"))

# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("\n")

# 2*i-1) = odd number series as if i = 2 it will print 3 so 1,3,5,7,9
# is i starts with = 2i+1 as it's start with 1 then 2i-1







# Q8 = Program to print in right angle

# n = int(input("Enter Number:   \n"))

# for i in range(1, n+1):
    
#     print("*"* i, end="")
#     print("\n")








# Q9 = Program to print the following pattern
#       * * *
# 
#       *   *
#     
#       * * *
#       n = 3






# n = int(input("Enter Number:   \n"))

# for i in range(1, n+1):
    # if(i==1 or i==n): # if i == 1 which means first row and last row as i==n which is n as number is typed by user 
        # print("*"*n, end="") # will print also number of * typed by user on the line = n and first line 
    # else:
        # print("*", end="") # Printing * once in second line
        # print(" "*(n-2), end="") # in mid o=f second line there is 1 space = n-2
        # print("*", end="") # Printing * once in second line

    # print("")
    









# Q10 = Program to print a table in reverse



# n = int(input("Enter Number:   \n"))

# for i in range(1, 11):
    
#     print(f"{n} X {i} = {n * i}")



# n = int(input("Enter Number:   \n"))

# for i in range(1, 11):
    
#     print(f"{n} X {11 - i} = {n * (11-i)}")

# 1 = 10
# 2 = 9
# 3 = 8 
# 4 = 7
# 5 = 6
# 6 = 5
# 7 = 4
# 8 = 3
# 9 = 2
# 10 = 1
 
 # original positions and now how we want them though both positions add up to 11 if we subtrat i from 11





