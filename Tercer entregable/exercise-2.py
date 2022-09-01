"""
    Analysis:

    1. Get the number.
    2. Check if the number is odd. repeat if not odd.
"""

# Welcome
print("Welcome to you odd program: ")


# False will turn into True, just a semantics issue.
odd = False
while not(odd):
    
    # Get the number.
    u_answer = input("""Write your number, I'll check if its odd. 
I'll let you go when you write an odd number: """) # Gets the user number.

    if u_answer.isdigit(): # Checks if it's a digit.
        if int(u_answer) % 2 == 1:
            print("\nIt's odd. You win\n")
            odd = True
        else: 
            print("\nIt's not odd\n")
    else: # In the case it is an ascii.
        print("\nThis is not even a number!\n")
