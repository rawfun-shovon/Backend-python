#Remove Comment """
""""
#Build a greeting program - Today's Assignment
name =input("Enter your name: ")
age = int(input("Enter your age: "))
#print("Hello ", name,'!')
#print("Your age next year will be",age+1)
next_year_age = age + 1
print(f'Hello {name}! Next year you will be {next_year_age}.')
print("")

'''1. Temperature converter
Ask the user for a temperature in Celsius, then print it in Fahrenheit using the
formula F = C * 9/5 + 32 . Remember to convert the input with float() '''
print('''Temperature converter''')
print("")
print('''Ask the user for a temperature in Celsius, then print it in Fahrenheit using the
formula F = C * 9/5 + 32 . Remember to convert the input with float()''')
print("")
print(f'Hello {name}!')
celsius = float(input("Enter your temperature in Celsius: "))
fahrenheit = ((9 * celsius) / 5)+32
print(f"The temperature is {fahrenheit} in Fahrenheit")

'''2. Simple bill calculator
Ask for a product's price and quantity, then print the total. 
Add a 5% tax on top and print the final amount too. Use meaningful variable names in snake_case .'''
print("")
print(''''Simple bill calculator''')
print("")

print('''Ask for a product's price and quantity, then print the total. 
Add a 5% tax on top and print the final amount too. Use meaningful variable names in snake_case .''')
print("")
"""
#Remove Comment upper line """

product = float(input("Enter your product's price: "))
quantity = int(input("Enter your quantity: "))
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

#Remove Comment """

"""
'''3. Odd or even checker
Ask the user for a whole number and print whether it is odd or even. Use the
modulo operator: number % 2 == 0 is True for even numbers.'''

print(''''Odd or even checker. 
Ask the user for a whole number and print whether it is odd or even. Use the
modulo operator: number % 2 == 0 is True for even numbers.''')

number= int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is Even")
else:
    print(f"The number {number} is Odd")
"""
#Remove Comment upper line """