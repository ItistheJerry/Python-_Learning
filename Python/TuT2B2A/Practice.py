# Q1 = program to display a user entered name followed by good morning
name = input("What Would You like me to call you sir:  ")
# print("Good Morning Mr.: ", name, "Hope You had a good Night Sleep") or
print(f"Good Morning Mr.: {name} .Hope You had a good Night Sleep")


# Q2 = Program to fill in a letter template given with name and date
letter = '''Dear <|Name|>,
            You are selected!
             <|Date|>'''


# .Replace chaining
print(letter.replace("<|Name|>", "Jerry").replace("<|Date|>", "14 November, 2050"))



# Q3 = Program to detect double space in a string

name = "My name is Jerry   wbu?"


# finds index of any substring
print(name.find("   "))


# Q4 = Program to replace the double space to single space
print(name.replace("   ", " "))
# name isn't changed, a new string is generated and then printed as strings are immutable
# Lists do change though

# Q5 = Program to format the folowing letter using escape sequence characters
# letter = "Dear Harry, this python course is looking easy so far, though it may seem easy but without practice it is going to be hard enough but no matter what I will give it my best. Thanks!"

letter = "Dear Harry, this python course is looking easy so far, though it may seem easy but without practice it is going to be hard enough \n but no matter what I will give it my best. Thanks!"

print("Dear Harry, this python course is looking easy so far, \nthough it may seem easy but without practice it is going to be hard enough \nbut no matter what I will give it my best. \nThanks!")

# capital letters used by classes string usually starts with small letters
# makes a recognisable pattern habit
