# Write your solution here
while True:
    num=int(input("Please type in a number: "))
    if num>0:
        print(num**0.5)
    elif num==0:
        print("Exiting...")
        break
    else:
        print("Invalid number")
