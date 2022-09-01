"""
    Analysis:

    1. Get data.
    2. Ask what to do.
    3. Execute the program.
"""

""" Solution: """


while True:
    
    # Asks the user what does he want to to do.
    u_answer = input("""What do you want to do? 
    1. Add both numbers.
    2. Substract both numbers.
    3. Multiply both nubmers.
    4. Stop the program.
Enter your choice: """)
    
     # Checks if its digit and if the answer is between 1-4.
    if u_answer.isdigit():
        if 1 <= int(u_answer) <= 4:
            
            # Ask what to do.
            if u_answer == '4':
                print("Thx for coming")
                break
                
            else:
            
                # Get numbers:
                num_1 = float(input("Write your first number: "))
                num_2 = float(input("Write your second number: "))

                
                if u_answer == '1':
                    math = num_1 + num_2
                    print(f"The result is: {math}.")

                elif u_answer == '2':
                    math = num_1 - num_2
                    print(f"The result is: {math}.")

                elif u_answer == '3':
                    math = num_1 * num_2
                    print(f"The result is {math}.")
                
        else:
            print("Error: It needs to be between 1 to 4")
                
    else: # If it's not digit, it will catch the error.
        print("Error: It needs to be a number.")
        continue

    # Execute the program - It checks the user answer and executes the operation.
    
