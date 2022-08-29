"""
    Analysis:

    1. Get data.
    2. Ask what to do.
    3. Execute the program.
"""

""" Solution: """

loop = True
while loop:

    # Get numbers:
    num_1 = float(input("Write your first number: "))
    num_2 = float(input("Write your second number: "))

    # Ask what to do.

    while True: # Starts the loop
        u_answer = input("""What do you want to do? 
        1. Add both numbers.
        2. Substract both numbers.
        3. Multiply both nubmers.
        4. Stop the program.
        """) # Asks the user what does he want to to do.

        if u_answer.isdigit(): # Checks if its digit and if the answer is between 1-4.
            if (int(u_answer) >= 1) and (int(u_answer) <= 4):
                u_answer = int(u_answer)
                break
            else:
                print("Error: It needs to be between 1 to 4")
        else: # If it's not digit, it will catch the error.
            print("Error: It needs to be a number.")
            continue

    # Execute the program - It checks the user answer and executes the operation.
    if u_answer == 1:
        math = num_1 + num_2
        print(f"The result is: {math}.")
    elif u_answer == 2:
        math = num_1 - num_2
        print(f"The result is: {math}.")
    elif u_answer == 3:
        math = num_1 * num_2
        print(f"The result is {math}.")
    else:
        print("Thx for coming")
        break