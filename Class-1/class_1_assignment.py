#Remove '#' from the (""") to comment the section
#Bookmark """
#""""

#Build a greeting program - Today's Assignment
name =input("Enter your name: ")
while True:
    try:
        age = int(input("Enter your age: "))            #except ZeroDivisionError:
        if age < 0:
            print("Your age cannot be negative! Please try again.")
            continue
        break
    except ValueError:                                  #except Exception:
        print("Please enter a numeric value.")
#print("Your age next year will be",age+1)
next_year_age = age + 1
print(f'Hello {name}! Next year you will be {next_year_age}.')
print("")

input("Press Enter for next problem.")
print("")

"""
#Bookmark """
#""""

'''1. Temperature converter
Ask the user for a temperature in Celsius, then print it in Fahrenheit using the
formula F = C * 9/5 + 32 . Remember to convert the input with float() '''

print('''\t Temperature converter''')
print("")
print('''\t Ask the user for a temperature in Celsius, 
\t then print it in Fahrenheit using the
\t formula F = C * 9/5 + 32 . 
\t Remember to convert the input with float()''')
print("")
#print(f'Hello {name}!')

while True:
    try:
        celsius = float(input("Enter your temperature in Celsius: "))
        break # right numbers are provided.
    except ValueError:
        print("Something went wrong! Please enter a numeric value.")

fahrenheit = ((9 * celsius) / 5)+32
print(f"The temperature is {fahrenheit} in Fahrenheit")

print("")
input("Press Enter for next problem.")
print("")

#"""
#Bookmark """
#"""

'''2. Simple bill calculator
Ask for a product's price and quantity, then print the total. 
Add a 5% tax on top and print the final amount too. Use meaningful variable names in snake_case .'''
print("")
print('''Simple bill calculator''')
print("")

print('''Ask for a product's price and quantity, then print the total. 
Add a 5% tax on top and print the final amount too. Use meaningful variable names in snake_case .''')
print("")

while True:
    try:
        product = float(input("Enter your product's price: "))
        quantity = int(input("Enter your quantity: "))
        break
    except ValueError:
        print("Something went wrong! Please enter a numeric value.")

total = float(product * quantity)
print(''''Product bill total:''', total)
print("")
tax_rate =0.05
print("")
print("Tax rate is 5%")
tax = float(total*tax_rate)
print("")
print("Total tax is $", tax)
final_price = float(total + tax)
print("")
print("Final price is $", final_price)

print("")
input("Press Enter for next problem.")
print("")

"""
#Bookmark """
#"""

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

print("")
input("Press Enter for next problem.")
print("")

"""
#Bookmark """
#"""
