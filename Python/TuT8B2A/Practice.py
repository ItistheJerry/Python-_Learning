# Q1 = Program to read the text from a given file = poems.txt and find out wheter it contains the word twinkle


# with open("/Users/thejoker/Desktop/Python/TuT8B2A/poem.txt") as p:
#     content = p.read()
#     if("Twinkle", "twinkle" in content):
#         print("Yes BaBaji")
#     else:
#         print("No BaBaji")





# Q2 = game() in a Program lets a user play a game and returns the score as an integer. You need to read a file hi-score.txt which is either blank or contains the previous hi-score you need to write a program to update the hi score whenever the game() function breaks the hi-score
# import random

# def game():
#     print("Game Loading.............")
#     print("Playing Game......")
#     score = random.randint(1, 60)
#     # Fetch the hiscore
#     # Here if the the file (hiscore) is empty than the score is 0, or if something then convert to int and save the score as f.read is in str
#     with open("/Users/thejoker/Desktop/Python/TuT8B2A/hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"Your Score: {score}")
#     if(score>hiscore):
#         # write this hiscore to the file
#         with open("/Users/thejoker/Desktop/Python/TuT8B2A/hiscore.txt", "w") as f:
#             f.write(str(score))
# # if score is higher than hiscore then it will write the new score
#     return score

# game()







# Q3 = Program to generate multiple table from 2 to 20 and write it to the different files. place these files in a folder for a 13 year old
# def generate(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n*i}\n" 
    
#     with open(f"/Users/thejoker/Desktop/Python/TuT8B2A/tables/table_{n}", "w") as f:
#         f.write(table)



# for i in range(2, 21):
#     generate(i)







# Q4 = a File contains "donkey Word" multiple times. you need to write a program to replace the word with #### by updating the same file

# word  = "Donkey"

# with open("/Users/thejoker/Desktop/Python/TuT8B2A/word.txt", "r") as f:
#     content = f.read()
# contentNew = content.replace("Donkey", "######")


# with open("/Users/thejoker/Desktop/Python/TuT8B2A/word.txt", "w") as f:
#     f.write(contentNew)















# Q5 = Repeat program 4 for a list of such words to be censored



# words  = ["Donkey", "Bad", "nude", "Fucker", "Thank You", "No"]

# with open("/Users/thejoker/Desktop/Python/TuT8B2A/word.txt", "r") as f:
#     content = f.read()



# for word in words:
#     content = content.replace(word, "#" * len(word))


# with open("/Users/thejoker/Desktop/Python/TuT8B2A/word.txt", "w") as f:
#     f.write(content)











# Q6 = Program to mine a log file and find out whether it contains 'python'

# with open("/Users/thejoker/Desktop/Python/TuT8B2A/log.txt") as f:
#     content = f.read()

# if("Python" in content):
#     print("Yes")
# else:
#     print("No")











# Q7 Program To find Python written on

# with open("/Users/thejoker/Desktop/Python/TuT8B2A/log.txt") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines:
#     if("Python" in line):
#         print(f"Yes Python is Present on Line no: {lineno} \n")
#         break
#     lineno += 1
    

# else:
#     print("No Python is Present: \n")
    
    
    







# Q8 = Program To make a copy of a text file "this.txt"




# with open("/Users/thejoker/Desktop/Python/TuT8B2A/this.txt") as f:
#     content = f.read()

# with open("/Users/thejoker/Desktop/Python/TuT8B2A/Copied_this.txt", "w") as f:
#     f.write(content) 









# Q9 = Program To find whether a file is identical and matches the content of another file


# with open("/Users/thejoker/Desktop/Python/TuT8B2A/this.txt") as f:
#     content1 = f.read()

# with open("/Users/thejoker/Desktop/Python/TuT8B2A/Copied_this.txt") as f:
#     content2 = f.read()

# if(content1 == content2):
#     print("Yes These Files are identical")
# else:
#     print("No They are Not")









# Q10 = Program to wipe out the content of a file using python

# File Path
file_path = "/Users/thejoker/Desktop/Python/TuT8B2A/Copied_this.txt"

# with open(file_path, "w") as f:
#     f.write("aAs")



# A Code to replace the above one works just fine


# # Read the content of the file
# with open(file_path, "r") as f:
#     content = f.read()
    

# # Replace "content" with "Do Not Follow" in the file's content
# new_content = content.replace("content", "Do Not Follow")



# # Write the modified content back to the file
# with open(file_path, "w") as f:
#     f.write(new_content)










# Q11 = Program To rename a file to "renamed_by_python.txt"

# Better option was to use os module but due to early entry in course could'nt use that one 

# with open(file_path) as f:
#     content = f.read()

# with open("/Users/thejoker/Desktop/Python/TuT8B2A/renamed_by_python.txt", "w") as f:
#     f.write(content)









