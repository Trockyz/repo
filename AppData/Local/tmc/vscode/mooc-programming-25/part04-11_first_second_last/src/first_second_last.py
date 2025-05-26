def first_word(word):
    x = word.find(" ")
    y = word[0:x]
    word = word[x+1:]
    return y

def second_word(word):
    x = word.find(" ")
    word = word[x:]
    y = word.find(" ")
    return word[:y]

def last_word(word):
    while word.find(" ") != -1:
        x = word.find(" ")
        lastword = word
        word = word[x+1:]
    return word

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
