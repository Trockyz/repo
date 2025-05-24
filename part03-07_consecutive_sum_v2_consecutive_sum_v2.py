result=0
x=1
lim=int(input("Limit: "))
consec_sum="The consecutive sum: "
while result<lim:
    if result+x+1<=lim:
        consec_sum+=f"{x} + "
    else:
        consec_sum+=f"{x} "
    result+=x
    x+=1
print(consec_sum+f"= {result}")