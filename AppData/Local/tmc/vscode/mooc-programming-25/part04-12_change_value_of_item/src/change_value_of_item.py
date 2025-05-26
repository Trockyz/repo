# Write your solution here
list=[1,2,3,4,5]
while True:
    ind=int(input("Index: "))
    if ind==-1:
        break
    val=int(input("New value: "))
    list[ind]=val
    print(list)