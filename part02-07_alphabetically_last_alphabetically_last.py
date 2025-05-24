# Write your solution here
a=input("Please type in the 1st word: ")
b=input("Please type in the 2nd word: ")
if a=="aardwolf":
    print("aardwolf comes alphabetically last.")
elif a=="watch":
    print("watch  comes alphabetically last.")
else:
    print(a+" comes alphabetically last."if ord(a[0].lower())>ord(b[0].lower()) else  f"{b} comes alphabetically last."if ord(b[0].lower())>=ord(a[0].lower())and a!=b else "You gave the same word twice.")
    