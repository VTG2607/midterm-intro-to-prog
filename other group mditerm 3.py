n = input()
while n != 'END':
    output = ''
    for character in n:
        if character != ' ':
            output += character
    print(output)
    n = input()