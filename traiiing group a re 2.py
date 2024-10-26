numbers = input('give a number')
count = 0
while numbers != '0':
    for number in numbers:
        if int(number) % 5 == 0:
            count += 1
    numbers = input()

print(count)