div_by_7 = 0
try:
    while True:
        data = input().split()
        for i in data:
            if int(i) % 7 == 0:
                div_by_7 += 1
except EOFError:
    print(div_by_7)