# determines whether or not a sentence is a palindrome
    # whether or not the sentence reads the same backwards   
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 24/09/2017
# Adapted from: https://stackoverflow.com/questions/19365008/python-function-to-check-for-palindrome

# user enters a sentence to be checked
sentence = input("Enter a sentence or word: ")


# 'sentence[::-1]' reverses the sentence
# the sentences are compared to see if they're the same
if sentence[::-1] == sentence:
    print("Sentence is a Palindrome!")

else:
    print("Sentence is not a Palindrome.")
    