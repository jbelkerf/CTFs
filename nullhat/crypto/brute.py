from math import gcd

for x in range(0, 1000000):
    g = gcd(x**13 + 37, (x+42)**13 + 37)
    if g > 100:
        print(x, g)
