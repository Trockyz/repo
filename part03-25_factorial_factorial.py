# Write your solution here
while True:
    num=int(input("Please type in a number:"))
    result=1
    x=1
    if num<=0:
        print("Thanks and bye!")
        break
    else:
        while x<=num:
            result*=x
            x+=1
        print(f"The factorial of the number {num} is {result}")