# Q1 = Program to find the greatest of four number entered by the user

# N1 = int(input("Enter number 1: "))
# N2 = int(input("Enter number 2: "))
# N3 = int(input("Enter number 3: "))
# N4 = int(input("Enter number 4: "))

# if(N1>N2 and N1>N3 and N1>N4):
#     print("Greatest number among all others is N1: ",N1)

# elif(N2>N1 and N2>N3 and N2>N4):
#     print("Greatest number among all others is N2: ",N2)

# elif(N3>N1 and N3>N2 and N3>N4):
#     print("Greatest number among all others is N3: ",N3)

# elif(N4>N1 and N4>N2 and N4>N3):
#     print("Greatest number among all others is N4: ",N4)

# else:
#     print("Ther is an error in your writing")


# print("End of Program")





# Q2  = Program to find whether a student has passed or failed it requires a total of 40% and alteast 33% in each subject to pass, Assume 3 subjects and take marks as an input from the user

# S1 = int(input("Enter Marks of Subject 1: \n"))
# S2 = int(input("Enter Marks of Subject 2: \n"))
# S3 = int(input("Enter Marks of Subject 3: \n\n"))

# p1 = S1/100*100
# p2 = S2/100*100
# p3 = S3/100*100

# print("Subject 1\n\n")

# if(p1>=40 and p1<=50):
#     print("The Student is Passed with: \n",p1)

# elif(p1>=51 and p1<=75):
#     print("The Student has Scored Average with: \n",p1)

# elif(p1>=76 and p1<=90):
#     print("The Student has scored Above average with: \n",p1)

# elif(p1>=91 and p1<=100):
#     print("The Student has scored TOP 10 highest with: \n",p1)

# else:
#     print("The Student has Failed\n\n")

# print("Subject 2\n\n")

# if(p2>=40 and p2<=50):
#     print("The Student is Passed with: \n",p2)

# elif(p2>=51 and p2<=75):
#     print("The Student has Scored Average with: \n",p2)

# elif(p2>=76 and p2<=90):
#     print("The Student has scored Above average with: \n",p2)

# elif(p2>=91 and p2<=100):
#     print("The Student has scored TOP 10 highest with: \n",p2)

# else:
#     print("The Student has Failed\n\n")

# print("Subject 3\n\n")

# if(p3>=40 and p3<=50):
#     print("The Student is Passed with: \n",p3)

# elif(p3>=51 and p3<=75):
#     print("The Student has Scored Average with: \n",p3)
# elif(p3>=76 and p3<=90):
#     print("The Student has scored Above average with: \n",p3)

# elif(p3>=91 and p3<=100):
#     print("The Student has scored TOP 10 highest with: \n",p3)

# else:
#     print("The Student has Failed\n")

# print("Thus Now Loading Overall Percentage of Student\n\n")

# Total = S1 + S2 + S3

# print("Loading Total.......... \n\n")

# print("The Total Marks of Student out of 300 is: \n\n",Total)

# Perc = Total/300*100

# print("Loading Percentage.......... \n\n")

# print("The Percentage Scored By Student is: \n\n",Perc)

# print("Hence\n")

# if(Perc>=40 and Perc<=50):
#     print("The Student is Passed with: \n\n",Perc)

# elif(Perc>=51 and Perc<=75):
#     print("The Student has Scored Average with: \n\n",Perc)

# elif(Perc>=76 and Perc<=90):
#     print("The Student has scored Above average with: \n\n",Perc)

# elif(Perc>=91 and Perc<=100):
#     print("The Student has scored TOP 10 highest with: \n\n",Perc)

# else:
#     print("The Student has Failed\n\n")


# print("End of Score Calculations\n\n")






# Q3 = A spam comment is defined as a text containing following keywords
# " Make a lot of money ", "Buy now ", " Subscribe this ", "Click this" 
# write a program to detect these spams.   

# in Keyword


# p1 = "Make a lot of money"
# p2 = "Buy now"
# p3 = "Subscribe this"
# p4 = "Click this" 



# message = input("Enter your comment: ")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("Spam Comment Detetcted :--------: TRY AGAIN! ")
# else:
#     print("The Comment you Typed is: ",message)






# Q4 = Program to find whether a given username contains less than 10 characters or not




# username = input("Enter Your Username: \n\n")

# if(len(username)>=10):
#     print("\nIt Contains 10 characters and more You may enter! \n")

# else:
#     print("\nTry Again The Username is short Try with atleast 10 Characters \n")







# Q5 = A program that checks whether a given name is present in a list or not

# list = ["Jerry", "Gun-Gun", "Samyak", "Iron-Knight", "Emperor-of-the-Known-Universe"]
# print("Note* The Name You know him By replace spaces with dash (-): \n\n")

# user = input("Enter Your name\n\n")
# name = input("Enter The Name You Know HIM By: \n\n")

# if(name in list):
#     print("You know HIM by: \n\n",name)
#     print("You may Enter MISTER: \n\n",user)
# else:
#     print("You May Try Again")








# Q6 = Program to calculate the grade of a student from his marks from the following scheme

# input = float(input("Enter Your Percentage:  \n\n"))

# print("\n\nYou Entered:  \n\n",input)


# print("\n\nLoading Grade.......\n\n")


# if(input >= 90):
#     print("According To Your Entered Score You Have Scored = A+\n\n")
# elif(input >= 80):
#     print("According To Your Entered Score You Have Scored = A\n\n")
# elif(input >= 70):
#     print("According To Your Entered Score You Have Scored = B\n\n")
# elif(input >= 60):
#     print("According To Your Entered Score You Have Scored = C\n\n")
# elif(input >= 50):
#     print("According To Your Entered Score You Have Scored = D\n\n")
# else:
#     print("According To Your Entered Score You Have Scored = F\n\n")


# print("Program Ended\n\n")
# print("Thank You For Your Patience\n\n")






# Q7 = Program to find Out whether a given post is talking About "Jerry" or not

# Keyword Finder

# post1 = "Hey Jerry, Your Wormhole Teleporter was Good\n"
# print(post1)
# print(post2)


# Checks in all forms of Jerry

# post = input("Enter Your Message\n")
# if("jerry" in post.lower()):
#     print("It Is There Man!\n")
# else:
#     print("You Don't Know Him\n")



