'''3. Odd or even checker
Ask the user for a whole number and print whether it is odd or even. Use the
modulo operator: number % 2 == 0 is True for even numbers.'''

print('''\t Odd or even checker. 
\t Ask the user for a whole number and print whether it is odd or even. 
\t Use the modulo operator: number % 2 == 0 is True for even numbers.''')

print("")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is Even")
else:
    print(f"The number {number} is Odd")
