import random
import math
input_number = int(input("n ="))
count_geometric_mean = 0
multiple_number = 1

for i in range(input_number):
    random_number = random.randint(20,70)
    print(random_number,end = ' ')            # end = ' ' to  put all output on the same line

    if random_number % 2 == 0:
        count_geometric_mean += 1
        multiple_number *= random_number
print(f"\nGeometric mean of the even values = {math.sqrt(multiple_number):.2f}")    #:.2f for two decimals

# \n for putting output values on the line below