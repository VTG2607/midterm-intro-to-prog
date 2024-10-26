n = input()
sum = 0
try:
    while True:
        for number in n:
            if int(number) % 2 != 0:
                sum += int(number)
        n = input()
except EOFError:
    print(sum)

    