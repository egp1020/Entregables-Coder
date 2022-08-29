"""
    Analysis:

    1. Get a number from the user from 0 to 9.
    2. Check if the number is in the list.
"""

# List of numbers
numbers = [1, 3, 6, 9]

# Ask the user for a number from 0 to 9.
while True:
    u_answer = input("Put a number from 0 to 9: ")
    if (u_answer.isdigit()) and (int(u_answer) >= 0 and int(u_answer) < 10):
        u_answer = int(u_answer)
        if u_answer in numbers:
            print(f"\nThe number {u_answer} exists in the list.\n")
            break
        else:
            print("\nThe number doesn't exist in the list.\n")
            break
    else:
        print("\nError: The number needs to be between 0 to 9\n")