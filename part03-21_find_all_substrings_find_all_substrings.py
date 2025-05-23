# Write your solution here
word=input("Please type in a word: ")
x=0
character=input("Please type in a character: ")
while True:
    if word.find(character)>=0 and word.find(character)<len(word)-2:
        print(word[word.find(character):word.find(character)+3])
        word=word[word.find(character)+1:]
    else:
        x+=1
    if x==len(word):
        break