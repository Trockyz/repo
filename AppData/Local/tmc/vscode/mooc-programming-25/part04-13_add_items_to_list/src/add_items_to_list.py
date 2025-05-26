# Write your solution here
list=[]
tick=1
itemcount=int(input("How many items: "))
while tick<=itemcount:
    tobeadded=int(input("Item "+str(tick)+": "))
    list.append(tobeadded)
    tick+=1
print(list)