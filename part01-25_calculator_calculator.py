numone=int(input("Number 1: "))
numtwo=int(input("Number 2: "))
operation=input("Operation: ")
if operation=="add":
    print(f"{numone} + {numtwo} = {numtwo+numone}")
if operation=="subtract":
    print(f"{numone} - {numtwo} = {numone-numtwo}")
if operation=="multiply":
    print(f"{numone} * {numtwo} = {numtwo*numone}")