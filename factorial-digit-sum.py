# calculates the factorial digit sum of 100 written in Python
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 20/09/2017
# Adapted from: http://www.pybloggers.com/2015/06/project-euler-20-factorial-digit-sum/

# initializes the counter at 1 
# so the first number multiplied is 1
cntr = 1

# the counter is incrementally multiplied by 'i'
for i in range(1, 101):
    cntr *= i

# splits the answer in a map using key:value pairs 
# and 'sums' them up
cntr = sum(map(int,str(cntr)))

# prints out the answer
print(cntr)