import random
import sys
import math
import collections

list = []
tot = 0

n = int(input())

for i in range(n):
    stdin = input()
    if (stdin == ""):
        list.append(tot)
        tot = 0
    else:
        tot += int(stdin)

list = sorted(list)
print(list[len(list) - 1])
print(list[len(list) - 1] + list[len(list) - 2] + list[len(list) - 3])
