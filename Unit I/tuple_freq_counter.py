"""
Tuple Frequency Counter

Author: Aryan Mahajan (1272261597)
Date Created: 2026-08-15
Unit: Unit I - Python Fundamentals & Data Structures

Description:
    Counts the frequency of 2D coordinate tuples within a list by mapping 
    each unique tuple to its occurrence count using a dictionary.
"""

print("") # formatting
print("") # formatting

coordinates = [(10, 20), (50, 80), (10, 20), (100, 150), (50, 80), (10, 20)]
print(f"Full List: {coordinates}")

counter = {}

# initialize dict
for i in range(len(coordinates)):
    counter[coordinates[i]] = 0

print("") # formatting

# finish counting
for j in range(len(coordinates)):
    if coordinates[j] in counter:
        counter[coordinates[j]] += 1

print(f"Prepared Dictionary: {counter}") 

print("") # formatting
print("") # formatting