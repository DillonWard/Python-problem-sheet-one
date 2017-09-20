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