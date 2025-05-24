# Write your solution here
password=input("Password: ")
while True:
    repeat=input("Repeat password: ")
    if repeat==password:
        print("User account created!")
        break
    else:
        print("They do not match!")
