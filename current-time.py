# imports 'localtime' and 'strftime' from the 'time' module
# localtime is used for getting the current local time
# strftime is used for displaying the current time in a string
from time import localtime, strftime

# prints the local time of the device
print(strftime("Current time: %a, %d %b %Y %H:%M:%S", localtime()))

# a%:abbreviated week day name, 
# %d:day of the month in decimals
# %b:abbreviated month name
# %Y:current year with century - 2017
# %H:%M:%S: current Hour, Minute, and Second 
