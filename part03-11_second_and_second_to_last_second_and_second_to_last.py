# Write your solution here
word=input("Please type in a string: ")
if word[1]!=word[len(word)-2]:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {word[1]}")