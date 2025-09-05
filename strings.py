
# Strings are immutable in Python

# To input a user's name and print good afternoon

# name = input("Enter  your name: ")
# print("Good Afternoon,", name) #No need to add extra space after Afternoon,", it automatically does it
# print(f"Good Afternoon, {name}") # use f for template literal
# date = input("Enter a date: ")

# This doesn't work
# letter = """
#     Dear {name},
#     You are Selected!
#     {date}"""

# letter = """
#     Dear {name},
#     You are Selected!
#     {date}"""
# print(letter.replace("|<name>|", name).replace("|<date>|", date)) #this work

# print(letter)


# doublestr = "This contains   double   spaces"
# print(doublestr.find("  ")) #finds the index of first double space, or -1 if not found


letter = "Dear User,\nYou are a genius. \nThanks for enrolling!"
print(letter)