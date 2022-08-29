"""
    Analysis:

    1. ask the user how many numbers does he want to create.
    2. Create a list with those numbers.
    3. Ask the user the numbers.
    4. add up al the numbers and do the average.
    5. Print the result.
"""

# Ask the quantity of numbers.
u_answer = input("How many numbers do you have to average?: ")
u_list = []

# Error catcher. This will be activated when the user puts a letter or a special character.
error_set = "abcdefghijklmnopq !\\\"'#$%&\'()*+-/:;<=>?@[\]^_`{|}~üéâäàåçêëèïîìæÆôöòûùÿø£×ƒáíóúñªº¿®¬½¼¡«»░▒▓│┤©╣║╗╝¢¥┐└┴┬├─┼ã╚╔╩╦╠═╬¤ðı┘┌█▄¦▀ßõµþý¯´≡±‗¾¶§÷¸°¨·¹³²■"
if set(u_answer).intersection(error_set):
    print("\nError: Your answer contains letters or special characters.\n")
    exit()

# Create a list with the numbers.
if u_answer.isdigit(): # Error catcher.
    for n in range(int(u_answer)): # It creates a list within the range of u_answer
        u_list.append(n)
else:
    print("\nError: Please restart the program and put an non-decimal number.\n") # Error catcher
    exit() # If the user puts a letter the program will be killed.



# Ask the numbers to put in the list.
for n in range(len(u_list)): # It will iterate from 0 until the length of the list.(Last number)
    u_answer = input(f"What is your number {n+1}?: ") # It will let the user know what number s/hes is in.
        # Changing float to string
    if set(u_answer).intersection(error_set): # Evaluates if the answer contains special chacarters
        print("\nError: Your answer contains letters or special characters.\n")
        exit()
    # Evaluates if the answer contains max 1 "." or "," and transform it to string.
    elif ([*u_answer].count(".") == 1) or ([*u_answer].count(",") == 1):
        u_answer = u_answer.replace(",", ".")
        u_answer = float(u_answer)
        u_list[n:] = [u_answer]
    elif u_answer.isdigit(): # Error catcher.
        u_list[n:] = [int(u_answer)] # It will start at n position and modify the number of the position.
    elif u_answer.isdecimal():
            u_list[n:] = [float(u_answer)] # It will start at n position and modify the number of the position.
    else:
        print("\nError: It needed to be a number. Restart the program.\n") # Error catcher.
        exit() # If the user puts a letter the program will be killed.

# Add up the numbers and do the average.
u_list = sum(u_list)/len(u_list)

# Print the result.
print(f"The average is {u_list}")