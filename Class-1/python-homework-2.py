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
print("Total tax is $", tax)
final_price = float(total + tax)
print("")
print("Final price is $", final_price)
