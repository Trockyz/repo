# Copy here code of line function from previous exercise
def line(num,str):
    if len(str)>0:
        print(str[0]*num)
    else:
        print("*"*num)
def triangle(size):
    # You should call function line here with proper parameters
    x=0
    while x<=size:
        line(x, "#")
        x+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(150)
