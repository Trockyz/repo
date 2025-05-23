# Write your solution here
x=0
y=0
width=int(input("Width: "))
height=int(input("Height: "))
while y!=height:
    while x!=width:
        print("#",end="")
        x+=1
    x=0
    print()
    y+=1
