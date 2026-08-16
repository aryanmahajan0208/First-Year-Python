"""
List Operations: Linear Search and Minima/Maxima Finder

Author: Aryan Mahajan (1272261597)
Date: 2026-08-11
Unit: Unit I - Python Fundamentals & Data Structures

Description:
    Demonstrates manual array traversal on an unsorted integer list:
    1. Linear search algorithm with early termination on match.
    2. Single-pass tracking of minimum/maximum elements and their indices.
"""

# sample dataset
x = [60, 10, 80, 40, 50, 30, 0, 100, 20, 90, 70]

# accepting key from user
key = int(input("Enter key to search for: "))

# linear search to check first appearance of key, returns -1 if key is not found
index = -1
for i in range(len(x)):
    if x[i] == key:
        index = i
        print(f"Key {key} found at index {i}")
        break

if index < 0: 
    print(index)

# minima and maxima finder, initialize min and max to first element of list 
min, min_index = x[0], 0
max, max_index = x[0], 0

for i in range(len(x)):
    if x[i] < min:
        min = x[i]
        min_index = i
    if x[i] > max:
        max = x[i]
        max_index = i
        
# print output
print(f"Max value is {max} at index {max_index}")
print(f"Min value is {min} at index {min_index}")