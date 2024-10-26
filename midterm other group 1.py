n = input('give a num')
product = 1
while n != '0':
    for number in n:
        if int(number) % 2 == 0:
            product *= int(number)
    n = input()

print(product)