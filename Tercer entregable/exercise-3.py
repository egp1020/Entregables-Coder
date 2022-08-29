"""
    Analysis:

    1. Create a list of numbers.
    2. Add up the list.
"""

# Solution

# Creating the list
list = []

for n in range(1, 101, 2):
    list.append(n)

# Add up the list
list = sum(list)
print(list)