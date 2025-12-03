# Day 2. Create a list of usernames
# Input a username from the user. Check if the username is present in the list or not

usernames = ["alice", "bob", "charlie", "david", "eve"]
name = input("Enter a username: ")
if name in usernames:
    print("Username found!")
else:
    print("Username not found.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Day 2. Create a dictionary of usernames and passwords, extract all the usernames from the dictionary and 	
# input username from the user and check if the username is present in the extracted list of 	usernames

user = {"alice": "password123",
        "bob": "qwerty",
        "charlie": "letmein",
        "david": "123456",
        "eve": "trustno1"}

# Extracting usernames
usernames = list(user.keys())
print("Extracted Usernames: ", usernames)
name = input("Enter a username: ")

if name in usernames:
    print("Username found!")
else:
    print("Username not found.")

# Update the login dictationary program using IF ELSE
username = input("Enter your username: ")
password = input("Enter your password: ")
if username in user:
    if user[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")