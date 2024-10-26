word = input()
new_word = ''
while word != 'END':
    new_word = '' # put inside loop to make it empty
    for character in word:
        if character.islower() is True:
            word = word.replace(character,'')# replace if nnothing to replace, removes characters
        else:
            new_word += character * 2
    print(new_word)
    word = input()


