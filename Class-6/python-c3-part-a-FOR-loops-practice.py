cart = [
    {"name": "Keyboard", "price": 200, "quantity": 2},
    {"name": "mouse", "price": 100, "quantity": 1},
]

#print(cart[0]["name"])      #keyboard
#print(len(cart))            #2 -how many items

'''if cart:                    # a non-empty list is truthy
    print("Cart has items")
else:
    print("No items found")'''

for item in cart:
    print(item)

# empty list
'''duc = [

]

if duc:                    # a non-empty list is truthy
    print("duc has items")
else:
    print("No items found")

for item in duc:
    print(item)'''

'''for ch in "Python":
    print(ch)

point = (23.8, 80.4)
for value in point:
    print(value)

for input_s in input("Enter something: ").split():
    print(input_s)'''

allowed_roles = ["admin", "user", "boss"]
for role in allowed_roles:
    if role not in ["admin", "user"]:
        print(role,"not allowed")
    else:
        print(role,"is allowed")

#6 LOOPING OVER DICTIONARIES

student = {
    "name": "Rahim",
    "age": 25,
    "department": "CSE"
}
for key in student:         #keys only
    print(key, "->", student[key])
print("")
for key, value in student.items():  # key and value together - cleanest
    print(key, ":", value)
print("")
for value in student.values():      # values only
    print(value)
print("")

users = [
    {"id": 1, "name": "Rahim", "age": 25},
    {"id": 2, "name": "Karim", "age": 17},
    {"id": 3, "name": "Hasan", "age": 31},
]

for user in users:
    if user["age"] >= 18:
        print(user["name"], "is an adult")
    else:
        print(user["name"], "is a minor")


#7 enumerate () and zip()
# Need the position and the item? enumerate() gives you both,
# so you never have to write 'range(len(...))' again:

names = ["Rahim", "Karim", "Hasan"]

for index, name in enumerate(names):
    print(index, name)

for index, name in enumerate(names, start=1):
    print(index, name)

