#Solution - 2
print("\n")
print('''\t 2. Does it exist?
\t Ask the user for a number, then check with in whether it's in a given list. 
\t Print a friendly yes/no message with if/else .''')
print("")
input_list1 = [ 10, 20, 30, 40, 50]
print(input_list1)

while True:
    try:
        user_input = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

if user_input in input_list1:
    print(f"Yes, the number {user_input} is in the list. ")
else:
    print(f"No, the number {user_input} is not in the list. ")
