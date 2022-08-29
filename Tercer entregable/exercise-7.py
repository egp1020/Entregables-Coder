"""
    Analysis:

    1. Find the words in the old lists, and create a new list.
"""

# Solution 1

list_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
list_2 = ["h",'o','l','a',' ', 'l','u','n','a']

list_3 = []
for n in list_1:
    for i in list_2:
        if n == i:
            list_3.append(n)
            list_3 = list(set(list_3))
print(list_3)

# Solution 2

list_3 = []
for n in list_1:
    for i in list_2:
        if (n == i) and not(n in list_3):
            list_3.append(n)
print(list_3)