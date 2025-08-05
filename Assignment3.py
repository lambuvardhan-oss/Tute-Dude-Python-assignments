#Task1
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
sample_number=int(input("enter the factorial number:"))
Result=factorial(sample_number)
print(f"factorial of {sample_number} is :{Result}")

#Task2
number=int(input("Enter a number:"))
import math
print("Square root:",math.sqrt(number))
print("Logarithm:",math.log(number))
print("sine:",math.sin(number))

