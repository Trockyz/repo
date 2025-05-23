# Write your solution here


print("Please type in integer numbers. Type in 0 to finish.")
count=0
negativecount=0
positivecount=0
sum=0
while True:
    number=int(input("Number: "))
    if number==0:
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {sum}")
        print(f"The mean of the numbers is {sum/count}")
        print(f"Positive numbers {positivecount}")
        print(f"Negative numbers {negativecount}")
        break
    else:
        if number>0:
            positivecount+=1
        if number<0:
            negativecount+=1
        count+=1
        sum+=number