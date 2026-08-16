"""
Dictionary Operations

Author: Aryan Mahajan (1272261597)
Date: 2026-08-16
Unit: Unit I - Python Fundamentals & Data Structures
Assignment: Assignment I

Description:
    Demonstrates fundamental dictionary CRUD operations in Python:
        1. Key-value insertion.
        2. Value modification.
        3. Element removal and key deletion.
"""

# initialize original dictionary
students = {
    1: "Aryan",
    2: "Vedant",
    3: "Yash",
    4: "Aum", 
}

# print the original dictionary
print(f"Original dictionary: {students}")

# perform creation, read, update, deletion on dict
students[5] = "Paras" # creation of key-value pair
print(f"Value associated with key 2 is: {students[2]}") # reading value at key 2
students[3] = "Yash P." # updating a value 
del students[4] # deleting a key-value pair

# print modified dict
print(f"Final Dictionary: {students}")