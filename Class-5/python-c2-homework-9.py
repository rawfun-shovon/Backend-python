#Safe key check
#Check whether a dictionary has an "email" key.
# Print it if present, otherwise "Email not found" — use .get() or in .

user_input = {
    "username": "admin",
    "password": "1234",
    "email": "email@localhost.com"
}

if "email" in user_input:
    print("email is present:", user_input["email"])
else:
    print("Email not found!")

#2nd method
user_input1 = {
    "username": "admin",
    "password": "1234",
    #"email": "email@localhost.com"
}

print(user_input1.get("email", "Email not found!"))
