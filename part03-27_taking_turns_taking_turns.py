# Write your solution here
num=int(input("Please type in a number: "))
x=0
while x!=num:
    x+=1
    print(x)
    if x!=num:
        print(num)
        num-=1
    else:
        break   