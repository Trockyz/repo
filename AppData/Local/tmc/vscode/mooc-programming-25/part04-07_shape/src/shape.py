# Copy here code of line function from previous exercise and use it in your solution
def line(num,str):
    if len(str)>0:
        print(str[0]*num)
    else:
        print("*"*num)
def shape(num1,char1,num2,char2):
    x=0
    while x<=num1:
        line(x,char1)
        x+=1
    x=0
    while x<num2:
        line(num1,char2)
        x+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")