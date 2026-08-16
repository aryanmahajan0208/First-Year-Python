"""
Choice Based Calculator

Author: Aryan Mahajan (1272261597)
Date Created: 2026-08-10
Unit: Unit I - Python Fundamentals

Description:
    Implements a menu-driven arithmetic calculator handling basic operations 
    with barebones input validation. 
"""

print("Choice Based Calculator")

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")      
print("4. Division")

# accept user input
user_choice = int(input("Enter choice: "))

# accept operands and perform requested operation 
if user_choice == 1:
    a = int(input("Enter operand 1: "))
    b = int(input("Enter operand 2: "))
    print("Result is: ", a+b)
elif user_choice == 2:
    a = int(input("Enter operand 1: "))
    b = int(input("Enter operand 2: "))
    print("Result is: ", a-b)
elif user_choice == 3:
    a = int(input("Enter operand 1: "))
    b = int(input("Enter operand 2: "))
    print("Result is: ", a*b)
elif user_choice == 4:
    a = int(input("Enter operand 1: "))
    b = int(input("Enter operand 2: "))
    print("Result is:", a/b)
else: 
    print("Invalid Input!")