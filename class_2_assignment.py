input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
input_list2 = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]

print("List 1 =",input_list1)
print("List 2 =",input_list2)

#slice_list1 = input_list1[0:5]
#slice_list1 = input_list1[1:5:2]
#print(slice_list1)

print("")
#SOLUTION 1 - .append(x) - Add x to the end
print(' #SOLUTION 1 - .append(x) - Add x to the end')
x = 'rawfun'
print("x =",x)
input_list1.append(x)
print(input_list1)

y = False
print("y =",y)
input_list2.append(y)
print(input_list2)
# But cannot do input_list2.append(y, x), need to use .extend for that

#SOLUTION 2 - .insert(x) - Insert x at index i
print("")
print ('#SOLUTION 2 - .insert(x) - Insert x at index i')

x = True; i = 3 # x value changed
print("x =",x)

print("i =",i)
input_list1.insert(i, x)
print(input_list1)  # here the data of x = 'rawfun' is present from the previously appended list

#SOLUTION 3 - .extend - Add each item of another list
print("")
print('#SOLUTION 3 - .extend - Add each item of another list')
print("")
input_list1.extend(input_list2)
print('the list is extended with list 2 values:', input_list1)

print("")
#SOLUTION 4 - .remove(x) - Remove the first matching x
print("SOLUTION 4 - .remove(x) - Remove the first matching x")
print("")
print("List 1 =",input_list1)
print("Current x =",x); print("")
#input_list1.remove(x)

print("#cannot remove boolean values as x = True which equals 1 so it will remove the first data instead causing error")
print(".remove(9) instead from List 2")
input_list1.remove(9)
print(input_list2)
input_list1.remove('rawfun')
print('remove "rawfun" from new list 1')
print(input_list1, "rawfun is removed")  # but cannot remove boolean values with .remove

print("")
#SOLUTION 5 - .pop(i) - Remove & return item at i (last if empty)
print("#SOLUTION 5 - .pop(i) - Remove & return item at i (last if empty)")
print("")
#Reset DATA
input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
input_list2 = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]
print("List 1 =",input_list1)
print("List 2 =",input_list2)
print("")
input_list1.pop(5)
input_list2.pop(3)
print(input_list1, '5th index 4 is removed')
print(input_list2, '3rd index 8 is removed')

print("")
#SOLUTION 6 -.sort() / .reverse() - Sort / reverse in place
#Reset DATA
input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
input_list2 = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]
print("List 1 =",input_list1)
print("List 2 =",input_list2)
print("")
input_list1.sort()
input_list2.sort()
print("List 1 is sorted =",input_list1)
print("List 2 is sorted =",input_list2)
print ("Following method in List Slicing Section 5 reverse ")
print("print reverse=",input_list2[::-1])
print("But list2 is = ",input_list2,"which did not change data")

print("#Reset DATA")
input_list1 = [1, 2, 2, 3, 3, 4, 5, 5]
input_list2 = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]
print("List 1 =",input_list1)
print("List 2 =",input_list2)
print("")
#1st method - Reverse
input_list1.reverse()
print("List 1 is reversed =",input_list1)
#2nd method - Reverse
input_list2.sort(reverse=True)
print("List 2 is reversed =",input_list2)

print("")
#SOLUTION 7 - .count(x) / .index(x) - Count occurrences / find position
print("#SOLUTION 7 - .count(x) / .index(x) - Count occurrences / find position")

