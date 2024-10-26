import random
n = int(input('give a range'))
sum = 0
for i in range(0,n):
    number = random.randint(15,65)
    print(number,end = ' ')
    if number % 2 == 0:
        sum += number

arith_mean = round(sum / n,2)
print('\n arithmatic mean is : ',arith_mean)