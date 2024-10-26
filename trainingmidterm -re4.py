import random
geometric_mean = 1
geometric_count = 0
n = int(input("range of elements"))
for i in range(0,n):
    number = random.randint(20,80)
    print(number,end=' ')
    if number % 2 == 0:
        geometric_mean *= number
        geometric_count += 1
print(f'Geometric mean is: {geometric_mean**(1/geometric_count)}')