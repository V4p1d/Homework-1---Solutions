# Write a program that receives two inputs from the terminal (using input()).
# One input is an integer, the other is a string. If the length of the string is equal to the
# value of the integer, the program terminates. Otherwise the program will ask the user to provide
# another integer. The program will keep asking for a number, until the length of the string and the value
# of the integer match each other.
# Example: string = "hello", integer = 4, output --> "Please provide another number"

myString = input("Write a string here: ")
myInteger = int(input("Write the number of words of the string: "))

while len(myString) != myInteger:
    myInteger = int(input("Please, write the number of words of the string: "))


print("Good work!")