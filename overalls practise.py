# n = input()
# sums = 0
# try:
#     while True:
#         for numbers in n:
#             if int(numbers) % 2 != 0:
#                 sums += int(numbers)
#         n = input() # must be outside of if loop for code to work( it will keeep taking from first input if not)
# except EOFError:
#     print(sums)


# number = input()
# count = 0
# while number != '0':
#     sep_num = number.split()
#     for number in sep_num:
#         if int(number) % 5 == 0:
#             count += 1
#     number = input()
# print(count)

import random
n = int(input("range of numbers"))
odd_count = 0
product = 1
for i in range(0,n):
    number = random.randint(30,80)
    print(number, end=' ')
    if number % 2 != 0:
        odd_count += 1
        product *= number
print(odd_count)


geometric_mean = product**(1/odd_count)

print("geometric mean is",geometric_mean)




