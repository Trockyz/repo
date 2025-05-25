# Write your solution here
def spruce(num):
    x=1
    y=0
    print("a spruce!")
    while y<num:
        print(" "*(num-y-1)+"*"*(x))
        x+=2
        y+=1
    print((" "*(num-1))+"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(75)