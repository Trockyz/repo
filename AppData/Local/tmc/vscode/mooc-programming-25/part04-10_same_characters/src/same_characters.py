# Write your solution here
def same_chars(word,num1,num2):
    x=len(word)
    if len(word)<=num1 or len(word)<=num2:
        return False
    else:
        if word[num1]==word[num2]:
            return True
        else: 
            return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))