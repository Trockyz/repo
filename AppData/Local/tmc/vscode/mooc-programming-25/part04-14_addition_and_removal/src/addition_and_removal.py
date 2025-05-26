# Write your solution here
listy=[]
tick=1
while True:
    print("The list is now "+str(listy))
    command=input("a(d)d, (r)emove or e(x)it: ")
    if command.lower()=="d":
        listy.append(tick)
        tick+=1
    elif command.lower()=="r":
        tick-=1
        listy.remove(tick)
    else:
        print("Bye!")
        break