# Write your solution here
wordone=input("Please type in string 1: ")
wordtwo=input("Please type in string 2: ")
if len(wordone)>len(wordtwo):
    print(wordone+" is longer")
elif len(wordtwo)>len(wordone):
    print(wordtwo+" is longer")
else:
    print("The strings are equally long")
