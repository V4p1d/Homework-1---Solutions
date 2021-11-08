# Write a program that receives two inputs from the terminal (using input()).
# Both inputs need to be an integer. Assign them, respectively to a variable named "n"
# and a variable named "p". The program will 
# compute the product n*nn*nnn*...*nnn...n (where the last number contains n written p number of times)
# and print it on the screen.
# example 1: n = 5, p = 4, output = 5*55*555*5555 = 847831875
# example 2: n = 3, p = 6, output = 3*33*333*3333*33333*333333 = 1220864470355308779

n = input("Insert n ")
p = int(input("Insert p "))

nNum = ""
mul = 1

for i in range(p):
    nNum = nNum + n
    mul = mul * int(nNum)

print(mul)