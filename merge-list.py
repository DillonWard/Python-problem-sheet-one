# merges and orders 2 lists together
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 24/09/2017

# import 'randint' from the 'random' module
from random import randint

# import 'merge' from the 'heapq' (heap queue) module
from heapq import merge

# initializes 2 empty lists
list_one = []
list_two = []

# the user enters the size of both lists
    # i.e 2 lists of 3
listLength = int(input("Enter length of the lists: "))

# loops and generates numbers randomly and inserts them into lists
for x in range(listLength):
    list_one.append(randint(1, 9))
    list_two.append(randint(1, 9))


# both of the lists are merged into one new list
# and are then 'sorted' using the sorted function
sorted_list = sorted(list(merge(list_one, list_two)))

print(sorted_list)