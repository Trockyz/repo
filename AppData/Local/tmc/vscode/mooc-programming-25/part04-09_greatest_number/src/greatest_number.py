# Write your solution here
def greatest_number(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    if num2>num1:
        if num2>num3:
            return num2
        else: 
            return num3
    if num3>num1:
        if num3>num2:
            return num3
        else:
            return num2
    else:
        return num2
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(8, 8, 8)
    print(greatest)