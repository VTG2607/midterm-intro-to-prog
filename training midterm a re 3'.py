string = input()
while string != 'END':
    word = ''
    for letter in string:
        if letter.isupper() is True:
            word += 2*letter
    print(word)
    string =input()