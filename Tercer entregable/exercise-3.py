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

# ------------------------ · Solution 2 · ------------------------

# Initializing variables.
_sum = 0

# Generating cycle.
for i in range(100):
    if i % 2 != 0:
        _sum += i

# Showing result.
print(f"La sumatoria es {_sum}.")

# ------------------------ · Solution 3 · ------------------------

suma = sum(range(1, 100, 2))

# Showing result.
print(f"La sumatoria es {suma}.")
