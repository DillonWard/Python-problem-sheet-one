# Python Problem Sheet One
###### *Dillon Ward - G00326756 - Emerging Technologies*
---

## Introduction
The following repository contains solutions to Python problem sheets for the module Emerging Technologies. The module is taught to undergraduate students at GMIT in the Department of Computer Science and Applied Physics. The lecturer is Ian McLoughlin.

## Prerequisites
* [git](https://git-scm.com/)
* [Python](https://www.python.org/downloads/)

## Cloning this Repository
To clone this repository and run the solutions, do the following:

```
In the command line change to a directory:
cd <directory>

Clone the repository:
git clone https://github.com/DillonWard/Python-problem-sheet-one.git

Change directory into the cloned folder:
cd <folder name>

*To ensure you're in the right folder, you can run the ls command to display all the files inside the folder. 
Files ending with 'py' are Python files.*
   
   
Run the program:
py <program name>.py
```

## Python
Python is an interpreted, interactive, object-oriented, widely used programming language that emphasizes code readability and allows programmers to express concepts in less lines of code in comparisson to other languages.
Python is popular for web development, big data, science, and scripting.  
Python comes with it's own standard libraries, and has a wide range of third-party libraries.

#### Pros
* Easy to learn/read
* Supports multiple platforms
* Object Orientated
* Large number of resources and libraries
* Uses less lines of code 

#### Cons
* Slow
* Limitations with database access
* Absence from Mobile Applications

### Why use Python?
#### Beginner Friendliness
Python was designed to be easy to read and understand. Python's layout has helped it become the most popular introductory language to new programmers. Since Python has a wide range of third-party libraries, it has a gradual learning curve that helps you build off the foundation of the basic funcionalitites.

#### Easy to Understand
The implication with Python is that anyone can come along and read it almost like English, which makes it easier for coding beginners. Since Python is a very high-level language, it is easy to read and understand.

### Installation
To install Python, you can head over to the Python [website](https://www.python.org/downloads/) and download the installer. The following solutions were coded using Python 3.

<a href="https://emerging-technologies.github.io/problems/python-fundamentals.html" target="_blank">Worksheet</a>
----

##### *The following list contains problems and solutions to the worksheet. Raw code can be found by following the solutions listed below.*
### Hello, World!
Write a program that prints “Hello, world!” to the screen.

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/hello-world.py" target="_blank">Solution</a>

### Current Time
Write a program that prints the current time and date to the console.

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/current-time.py" target="_blank">Solution</a>

### FizzBuzz
Write a program that prints the numbers from 1 to 100, except for the following conditions. For multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/fizzbuzz.py" target="_blank">Solution</a>

### Factorial Digit Sum
Write a function that calculates the sum of the digits of the factorial of a number. n! means n x (n − 1) … x 3 x 2 x 1. For example, 10! = 10 x 9 x … x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/factorial-digit-sum.py" target="_blank">Solution</a>

### Guessing Game
Write a guessing game where the user must guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/guessing-game.py" target="_blank">Solution</a>

### Largest and Smallest in List
Write a function that returns the largest and smallest elements in a list.

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/largest-and-smallest.py" target="_blank">Solution</a>

### Palindrome Test
Write a function that tests whether a string is a palindrome.

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/palindrome-test.py" target="_blank">Solution</a>

### Merge List and Sort
Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/merge-list.py" target="_blank">Solution</a>

### Newton's Method of Square Roots
Implement the square root function using Newton’s method. In this case, Newton’s method is to approximate sqrt(x) by picking a starting point z and then repeating:

`z_next = z - ((z*z - x) / (2 * z))`

To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, …). Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?

<a href="" target="_blank">Solution</a>

### Reverse String
Write a function to reverse a string.

<a href="https://raw.githubusercontent.com/DillonWard/Python-problem-sheet-one/master/reverse-string.py" target="_blank">Solution</a>
