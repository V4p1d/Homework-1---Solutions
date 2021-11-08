# Write a program that receives an input from the terminal (using input()).
# This input needs to be a string. If the string is "This is the right string." the program ends.
# Otherwise it keeps printing "Please provide the right string" until the string "This is the right string." 
# is provided.

string = input("Write the right string: ")

while string != "This is the right string.":
    string = input("Please provide the right string ")