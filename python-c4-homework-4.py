input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
print("The list is = ",input_list1)
print("After removing duplicates,",set(input_list1))

print("")
input("Press Enter to continue...")
print("")

a = {1, 2, 3, 4, 5}
b = {2, 8, 6, 8, 9, 7}
print("The list is = ",a)
print("The list is = ",b)

print("")
input("Press Enter to continue...")
print("")

print("a | b = ", a | b)  #union        ( everything )         = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("a & b = ", a & b)  #intersection ( common )             = {2}
print("a - b = ", a - b)  #difference   ( in a, not b)         = {1, 3, 4, 5}
print("a ^ b = ", a ^ b)  #symmetric    ( not shared)          = {1, 3, 4, 5, 6, 7, 8, 9}


