# Write your solution here
num=int(input("Please type in a number: "))
x=0
while True:
    if x+2<=num:
        x+=2
        print(x)
        print(x-1)
    elif x+1<=num:
        x+=1
        print(x)
    else: 
        break
