word = input("Please type in a string: ")
subword = input("Please type in a substring: ")

first_index = word.find(subword)
if first_index == -1:
    print("The substring does not occur twice in the string.")
else:
    # Start searching after the end of the first occurrence (non-overlapping)
    second_index = word.find(subword, first_index + len(subword))
    if second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")
