# Copy here code of line function from previous exercise
def line(num,str):
    if len(str)>0:
        print(str[0]*num)
    else:
        print("*"*num)
def box_of_hashes(height):
    # You should call function line here with proper parameters
    x=0
    while x!=height:
        line(10, "#")
        x+=1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(2)
