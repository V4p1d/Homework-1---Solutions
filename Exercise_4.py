# Write a program that receives three inputs from the terminal (using input()).
# These inputs needs to be integers. The program will print on the screen the sum of these three inputs.
# However, if two of the three inputs are equal, the program will print the product of these three inputs.
# Example 1: n = 1, m = 2, l = 3, output = 1 + 2 + 3 = 6
# Example 2: n = 1, m = 2, l = 2, output = 1 * 2 * 2 = 4

n = int(input("Provide the first number "))
m = int(input("Provide the second number "))
l = int(input("Provide the third number "))

if n == m or n == l or m == l: 
    print(n * m * l)
else: 
    print(n + m + l)
    