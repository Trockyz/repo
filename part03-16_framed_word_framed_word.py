# Write your solution here
word=input("Word: ")
def framed_word(word):
    width = 30
    padding_total = width - 2 - len(word)  # 2 for the '*' on each side
    padding_left = padding_total // 2
    padding_right = padding_total - padding_left

    # Create the frame lines
    top_bottom = '*' * width
    middle = '*' + ' ' * padding_left + word + ' ' * padding_right + '*'

    return f"{top_bottom}\n{middle}\n{top_bottom}"
print(framed_word(word))