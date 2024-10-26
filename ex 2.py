div_by_7 = 0
try:
    while True:
        n = input()   #don't put input outside the loop if run
        for a in n.split():
            try:
                if int(a) % 7 == 0:
                    div_by_7 += 1
            except ValueError:
                    pass
except EOFError:
    pass
print(div_by_7)
