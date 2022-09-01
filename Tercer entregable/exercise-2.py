"""
    Analysis:

    1. Get the number.
    2. Check if the number is odd. repeat if not odd.
"""

# Welcome
print("Welcome to you odd program: ")

# Get the number.
odd = False

while not(odd): # False will turn into True, just a semantics issue.
    u_answer = input("""Write your number, I'll check if its odd. 
I'll let you go when you write an odd number: """) # Gets the user number.

    # Checks if it's a digit.
    if u_answer.isdigit(): 
        if int(u_answer) % 2 == 1:
            print("\nIt's odd. You win\n")
            odd = True
        else: 
            print("\nIt's not odd\n")
            
    # In the case it is an ascii.
    else: 
        print("\nThis is not even a number!\n")
