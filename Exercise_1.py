# Write a program that receives an input from the terminal (using input()).
# This input needs to be an integer. Assign it to a variable named "n". The program will 
# compute the product n*nn*nnn and print it on the screen.
# example: n = 5 output = 5*55*555 = 152625


a = input("Insert n ")

num1 = int(a)
num2 = int(a + a)
num3 = int(a + a + a)

print(num1 * num2 * num3)