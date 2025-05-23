# Write your solution here
count=1
while True:
    pin=int(input("PIN: "))
    if pin !=4321:
        count=count+1
        print("Wrong")
    else:
        if count==1:
            print("Correct! It only took you one single attempt!")
            break
        else:
            print(f"Correct! It took you {count} attempts")
            break