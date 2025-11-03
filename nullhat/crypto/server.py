#!/usr/bin/env python3
from math import gcd
import os

flag = os.environ.get("FLAG", 'ELITESEC{1337_+_42_____________________________5}')
x = int(input("Enter x = "))
print(flag[:gcd(x**13 + 37, (x + 42)**13 + 37)])
