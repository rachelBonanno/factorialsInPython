# Factorials In Python (for Discreate HW3)
BONUS-8.6**: The Scottish mathematician James Stirling found an approximation formula for n!. Stirling's formula is $n!  \approx \sqrt{2 \pi n} n^n e^{-n}$ where $\pi$ = 3.14159 ... and e = 2.71828 .... (Scientific calculators have a key that computes ex; this key might be labeled exp x.) Compute n! and Stirling's approximation ton! for n = 10, 20, 30, 40, 50. What is the relative error in the approximations?

**For credit on this bonus problem, write code that will compute both n! and Stirling’s approximation of n! (rounded to the nearest integer) for a given n $\in$ N. (a) Show both the code and the input/output for n = 10, 20, 30, 40, 50 if possible. (b) Give the relative error (= error/correct value) to two significant digits, either as a decimal or a percent.


INPUT: 
```
import math
num = [10, 20, 30, 40, 50]
factorial = 1
for val in num:
    if val < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif val == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,val + 1):
           factorial = factorial*i
       print("The factorial of",val,"is",factorial,"and the relative error is", (factorial-math.sqrt(2*math.pi*val)*((val/math.e)**val))/factorial, "\n")
    factorial = 1
```

OUTPUT:
```
The factorial of 10 is 3628800 and the relative error is 0.008295960443938127 

The factorial of 20 is 2432902008176640000 and the relative error is 0.0041576526228797 

The factorial of 30 is 265252859812191058636308480000000 and the relative error is 0.002773820760111162 

The factorial of 40 is 815915283247897734345611269596115894272000000000 and the relative error is 0.002081121395979708 

The factorial of 50 is 30414093201713378043612608166064768844377641568960512000000000000 and the relative error is 0.0016652563663756474 
```
