# Write your solution here


word=input("Please type in a word: ")
character=input("Please type in a character: ")
if word.find(character)!=-1 and word.find(character)<len(word)-2:
    print(word[word.find(character):word.find(character)+3])