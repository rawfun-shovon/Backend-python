#Voting eligibility
#   Given an age and a boolean is_citizen , print whether the person can vote —
#   must be 18+ and a citizen (use and ).

citizen = [
    {"name": "Rawfun",     "age": 25, "is_citizen" : True},
    {"name": "Shovon",     "age": 17, "is_citizen" : True},
    {"name": "Not-Rawfun", "age": 12, "is_citizen" : False},
    {"name": "Not-Shovon", "age": 19, "is_citizen" : True},
]
print(citizen)
print("")
print(type(citizen))
print("")

for i in range(0, len(citizen)):
    if citizen[i]["age"] >= 18 and citizen[i]["is_citizen"]:
        print(citizen[i]["name"], " is eligible to vote")
    else:
        print(citizen[i]["name"]," is not eligible to vote")

