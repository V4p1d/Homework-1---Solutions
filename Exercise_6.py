# Write a program that receives an input from the terminal (using input()).
# The input needs to be an integer. The program will print on the terminal the difference between
# 24 and this input. If the input is greater than 24, then the program will compute the cube of the absolute
# value of the difference between 24 and the input.
# Example 1: input = 5, output = 19
# Example 2: input = 26, output = 8

myNumber = int(input("Please write an integer here: "))

if myNumber > 24: 

    print(abs(24 - myNumber)**3)
    # no need to use the function abs() here, this can be also solved with
    # print((myNumber - 24)**3), as myNumber is always greater than 24
else: 

    print(24 - myNumber)