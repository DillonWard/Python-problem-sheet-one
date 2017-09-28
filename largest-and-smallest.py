# returns the largest and smallest elements in a list
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 22/09/2017

# initializes a blank list to be populated
nums = []

# user input takes in the size of the list 
# the input is made into an int
listLength = int(input("Enter length of list: "))

# loops based off the list size
# the takes in numbers and the numbers are appended to the list
for x in range(listLength):
    number = input("Add a number to the list: ")
    nums.append(number)

# uses the 'max()' and 'min()' functions to display the smallest and largest in the list
print("\nLargest in the list \t:", max(nums), "\nSmallest in the list \t:", min(nums))
