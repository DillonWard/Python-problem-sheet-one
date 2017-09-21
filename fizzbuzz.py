# "FizzBuzz" problem written in Python
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 19/09/2017
# loops between the range of 1 and 101
for i in range(1, 101):

    # if 'i' being divisible by 3 and 5 is true, print out FizzBuzz 
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        # check for both 3 and 5 first
        # otherwise it'll print out 'Fizz' or 'Buzz' when 'i' reaches 15
        # depending on which comes first in the if statement

    # if 'i' being divisible by 3 is true, print out Fizz
    elif i % 3 == 0:
        print ("Fizz")

    # if 'i' being divisible by 5 is true, print out Buzz
    elif i % 5 == 0:
        print("Buzz")
    
    # otherwise, print out 'i'
    else:
        print(i)