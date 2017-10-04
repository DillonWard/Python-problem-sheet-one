# newton's method for square roots
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 03/10/2017
# import the math module
import math

# used for temporarily storing a value for comparrison
temp = 0.0

# initial variable passed into the function
z = 1.0

# user enters number
x = float(input("Enter number: " ))


# formula for calculating the square root
z_next = lambda z: z - ((z*z - x) / (2 * z))


while z != temp:
    # sets the temporary value
    temp = z
    # passes z into the formula
    z = z_next(z)
    print(z)

    # continuously loops until the previous number is the same
    # as the square root of the number passed in
    if(math.sqrt( x ) == z):
        break