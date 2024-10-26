import random
n = int(input("input a range"))
geometric_count = 0
product = 1
for i in range(0,n):
    number = random.randint(30,80)
    print(number,end = ' ')
    if number % 2 != 0:
        geometric_count += 1
        product *= number

geometric_mean = round(product**(1/geometric_count),3)


print("\ngeometric mean is: ",geometric_mean)


