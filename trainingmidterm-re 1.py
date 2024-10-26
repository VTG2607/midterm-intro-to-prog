n = input()
sum = 0
while n != '0':
    for i in n:
        if int(i) % 2 == 0:
            sum += int(i)
    n = input()
print(sum)