'''4. Break it, then fix it'''
print('''\t Break it, then fix it''')
print("")
print('''\t Write a program that intentionally causes a TypeError 
\t (hint: add a number to a string from input() ). 
\t Run it, copy the error message into a comment, 
\t then fix the code so it works. 
\t This trains you to read errors — the most important debugging skill.''')
print("")

#input1 = int( input("Type a string:")) # I opted to do string into an integer.
print("")

r'''
Traceback (most recent call last):
File "D:\Backend Engineering\Class 2\class_1_assignment.py", line 135, in <module>
input1 = int( input("Type a string:")) # I opted to do string into an integer.
ValueError: invalid literal for int() with base 10: 'sda'
'''

while True:
    try:
        input1 = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number: ")
print("")
