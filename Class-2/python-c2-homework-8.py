#8 Login system
#   Store a username and password, ask the user to enter them,
#   and print success or failure using and.

user = {
    "username": input("Enter your username: "),
    "password": input("Enter your password: "),
}
print(user["username"])
print(user["password"])

print("")

while True:
    login_user = input("Enter your username: ")
    login_password = input("Enter your password: ")

    if user["username"] == login_user and user["password"] == login_password:
        print("")
        print("Success! You've logged in!")
        break
    else:
        print("Failed! Try again!")
        print("")




