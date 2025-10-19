# Simple Login Form Program


users = {
    "ahmed": "1234",
    "sara": "abcd",
    "bilal": "pass123",
    "fatima": "hello123",
    "zain": "4321"
}


username = input("Enter your username: ")
password = input("Enter your password: ")


if username in users and users[username] == password:
    print("Login Successful!")
else:
    print("Login Failed. Invalid username or password.")
