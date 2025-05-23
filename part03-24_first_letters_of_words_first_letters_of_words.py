# Write your solution here
# print,find,cut
word=input("Please type in a sentence: ")
x=0
while x>=0:
    print(word[0])
    x=word.find(" ")
    word=word[x+1:]
