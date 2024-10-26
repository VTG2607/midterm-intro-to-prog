word = input()
while word != 'END':
    output = ''
    for letter in word:
        if letter.isupper() is True:
           output += letter
    print(output)
    word = input()
