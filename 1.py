sum_of_even_digits = 0

while True:
    number = input("Enter a multiple digit")
    if number == '0':
        break
    for digit in number:
        if int(float(digit)) % 2 == 0:
            sum_of_even_digits += int(float(digit))
print(sum_of_even_digits)
