# Write your solution here
while True:
    phrase=input("Editor:")
    if phrase.lower()=="notepad" or phrase.lower()=="word":
        print("awful")
    elif phrase.lower()=="visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")