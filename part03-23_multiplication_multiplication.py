# Write your solution here
num1=1
num2=1
req=int(input("Please type in a number: "))
while num2<=req:
    print(f" {num2} x {num1} = {num1*num2}")
    if num1 ==req:
        num2+=1
        num1=0
    num1+=1