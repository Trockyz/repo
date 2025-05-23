# Write your solution here
finalword=""
prevword=""
while True:
    word=input("Please type in a word: ")
    if prevword!=word and word!="end":
        finalword=finalword+" "+word
        prevword=word
    else:
        print(finalword[1:len(finalword)])
        break