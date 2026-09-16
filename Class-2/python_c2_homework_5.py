#Dictionaries — Key → Value Data
#Skip to line no. 75 for problem solution

"""A dictionary stores data as key–value pairs. Instead of a numeric index, you look items up by a
meaningful key:""" #dict_name = { key : value}
import copy

#Add '#' before """ in line no. 62 to turn off comment
#Bookmark """
"""
#Dictionary Example: Nested Data -> coded with suggestion from pycharm
student_data = [
    student1 := dict(
    id=101,
    name="Rawfun",
    address={
        "city": "Dhaka",
        "country": "Bangladesh",
    },
    age=10, department="CSE", cgpa=3.5),
    student2 := dict(
        id=202,
        name="Shovon",
        address={
            "city": "Oklahoma City",
            "country": "United States",
        },
        age=99, department="CS", cgpa=3.6)
]
print("")
print(student1["name"])     #not safe, could crash if key missing
print(student2.get("name")) #Safer; The value, or NONE if key missing
print("")
#print(student.keys())
#print(student.values())
print(student1.items())
#student_copy = student1.copy()
student_copy = copy.deepcopy(student1)
print("Removing 'name' from copy and returns its value =",student_copy.pop("name"))
print("")
print("Original items = ",student1.items())

print("")
input("Press Enter to continue...")
print("")

print(student_data[0]["name"])
print("")
print(student_data[1]["address"]["city"])

print("")
input("Press Enter to continue to problem...")
print("")

'''Go Deeper — this IS JSON
A “list of dictionaries” is almost exactly the JSON that web APIs send and receive. When you build
APIs later, you'll be shaping Python lists and dicts and handing them out as JSON. Learning this
structure now pays off directly.'''

"""
#Add '#' before """ in line no. 62 to turn off comment
#Bookmark """
"""

# simple example

users = [
    {"name": "Rawfun", "age": 25, "department": "CSE"},
    {"name": "Shovon", "age": 25, "department": "CSE"},
]
print(users[1]["name"])

"""
#Bookmark """
#"""
#Problem 5

student = {
    "name": "Rawfun",
    "age": 25,
    }
print(student["name"])
print(student["age"])
