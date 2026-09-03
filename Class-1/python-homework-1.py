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
