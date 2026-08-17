"""
Numeric Dataset Analyzer

Author: Aryan Mahajan (1272261597)
Date: 2026-08-17
Unit: Unit II - Control Structures & Functions

Description:
    Implements a reusable statistical summary function that calculates
    the minimum, maximum, and arithmetic mean of a numeric list and
    returns the aggregated metrics as a structured dictionary.
"""

def dataset_analyze(numbers):
    """
    Function to analyze a list of numbers or floats and return their 
    minima, maxima, and mean as a dictionary
    """
    if len(numbers) > 0:
        properties = {
            "min": 0,
            "max": 0,
            "mean": 0,
        }

        min_num = numbers[0]
        max_num = numbers[0]
        sum = 0

        for i in range(len(numbers)):
            if numbers[i] < min_num:
                min_num = numbers[i]
            if numbers[i] > max_num:
                max_num = numbers[i]
            sum += numbers[i]

        mean = sum / len(numbers)
            
        # assign values to keys
        properties["min"] = min_num
        properties["max"] = max_num
        properties["mean"] = mean

        
        return properties
    else:
        return "None"

user_in = []

for j in range(10):
    inp = int(input("Enter element: "))
    user_in.append(inp)

print(dataset_analyze(user_in))