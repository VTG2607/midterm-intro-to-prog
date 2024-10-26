try:
    while True:
        user_input = input("Enter numbers separated by spaces (EOF to exit): ")
        numbers = user_input.split()
        count = 0

        for number in numbers:
            try:
                num = int(number)
                if num % 7 == 0:
                    count += 1
            except ValueError:
                pass

        print(f"Count of numbers divisible by 7 in this line: {count}")
except EOFError:
    pass