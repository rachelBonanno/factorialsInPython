# Python program to find the factorial of a number provided by the user.
# To take input from the user
# int(input("Enter a number: "))
import math

num = [10, 20, 30, 40, 50]
factorial = 1

for val in num:
    # check if the number is negative, positive or zero
    if val < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif val == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,val + 1):
           factorial = factorial*i
       print("The factorial of",val,"is",factorial,"and the relative error is", (factorial-math.sqrt(2*math.pi*val)*((val/math.e)**val))/factorial, "\n")
    factorial = 1
