'''5 Explore memory with id()'''
print('''\t 5. Explore memory with id()''')
print("")

print('''\t Create a = 200 and b = 200 , then print a is b . 
\t Do the same with 2000 . In a comment, explain in one line 
\t why one prints True and the other False 
\t (revisit the small-integer cache in Section 11).''')
print("")

a = 200; b = 200
print(" a = 200, id(a) = ",id(a))
print(" b = 200, id(b) = ",id(b))
print("")
print(" a is b = ", id(a) is id(b))
#print(" a is b = ", a is b)

a = 2000; b = 2000
print(" a = 2000, id(a) = ",id(a))
print(" b = 2000, id(b) = ",id(b))
print("")
print(" a is b = ", id(a) is id(b))
