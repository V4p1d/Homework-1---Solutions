# Write a program that receives one input from the terminal (using input()).
# The input needs to be an integer. The program will compute the factorial of 
# this number and print it on the screen. If the number is negative the program will print 
# "Factorial does not exist for negative numbers". Remember that the factorial of 0 is 1.
# Example: input = 5, output = 5*4*3*2*1 = 120

myNumber = int(input("Please, provide an integer: "))

fact = 1

if myNumber >= 0:
    for i in range(1,myNumber + 1):
        fact *= i # this is equivalent to fact = fact * i
    print("The factorial of " + str(myNumber) + " is " + str(fact))

else: 
    print("Factorial does not exist for negative numbers")

