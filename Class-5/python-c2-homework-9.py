#Safe key check
#Check whether a dictionary has an "email" key.
# Print it if present, otherwise "Email not found" — use .get() or in .

user_input = {
    "username": "admin",
    "password": "1234",
    "email": "email@localhost.com"
}

if "email" in user_input:
    print("email is present")
else:
    print("Email not found!")
