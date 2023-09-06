import sys

try:
    num1 = int(input("input number:  "))
    num2 = int(input("input number:  "))
except ValueError:
    print("Error: invalid input")
    sys.exit(1)

try:
    result = num1 / num2
except ZeroDivisionError:
    print("Error: cannot divide by zero")
    sys.exit(1)
    
print(result)
