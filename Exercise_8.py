# Write a program that receives two inputs from the terminal (using input()).
# Both inputs need to be integers. Assign them, respectively to a variable named "m"
# and a variable named "n". The program will print on the terminal, the greatest common divisor (GCD)
# of the two numbers.
# Example: n = 10, m = 12, output = 2
# Hint1: use a list to contain the divisors of n and one to contain the divisors of m. Use the method append() 
# to add elements to the lists.
# Hint2: there is a very smart and quick implementation of this that can be found online. I'd recommend to try and 
# come up with your own version


n = int(input("First number: "))
m = int(input("Second number: "))

# if n == m the GCD is obviously the value of the numbers itself
if n == m:
    print("The GCD is " + str(n))

else:

    # Create three lists, one for the divisors of n, one for the divisors of m and 
    # one for the common divisors. Add the elements to these lists using the modulo and the in operators.
    nDivisors = []
    mDivisors = []
    commonDivisors = []

    for i in range(1, n + 1):
        if n%i == 0:
            nDivisors.append(i)

    for j in range(1, m + 1):
        if m%j == 0:
            mDivisors.append(j)


    # check which one is the smallest number
    if n > m:
        for div in mDivisors:
            if div in nDivisors:
                commonDivisors.append(div)

    else: 
        for div in nDivisors:
            if div in mDivisors:
                commonDivisors.append(div)

    # The largest divisor is going to be the last element added to the list. 
    # Notice that 1 is always added to the list.

    print("The GCD is " + str(commonDivisors[-1]))


    # This problem could have been solved using three lines in total using functions, recursion and the 
    # Eucledian algorithm. Link to the algorithm.
    # https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm 

