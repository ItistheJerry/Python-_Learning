# File I/O



# The Randam Access Memory is volatile and all its contents are lost once a program terminates in order to persist the data forever, we use files


# A file is a data stored in a storage device, a Python program can talk to the file by reading content from it and writing content in it 




# Types of Files


# Text File
# Binary File

# f = open("/Users/thejoker/Desktop/Python/TuT8B2A/f.txt") # opens file
# data = f.read() # Reads file
# print(data) # Prints data
# f.close # duty to close it 







# writing a File


# st = ("Hey Jerry You are a genius")


# f = open("mf.txt", "w") # opens and is given access to write

# f.write(st)  # Now we have given the data we need it to write
# f.close # duty calls





# Type = readline(f) = Reads every single line is a built in function

# MODES

# = r = open for reading and is in default with opne()
# = w = opne for writing and has to be declared
# = a = open for appending and adds anything at the end of the line
# = + = open for updating
# ='rb'= will open for read in binary mode
# ='rt'= will open for read in text mode and is in Default




# f = open("/Users/thejoker/Desktop/Python/TuT8B2A/f.txt")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5, type(line5))

# line6 = f.readline()
# print(line6, type(line6))



# using While Loop

# line = f.readline()
# while(line != ""):
#     print(line, type(line))
#     line = f.readline()

# f.close()






# How to Write in Python






# With Statement




# f = open("/Users/thejoker/Desktop/Python/TuT8B2A/f.txt")

# print(f.read())
# f.close()
# not to use f.close



# the same can be written using with statement


with open("/Users/thejoker/Desktop/Python/TuT8B2A/f.txt") as f:
    print(f.read())


# Do not need to explicitly close the code