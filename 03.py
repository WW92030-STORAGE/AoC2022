import random
import sys
import math
import collections

n = int(input())

res = 0
res2 = 0
for i in range(n):
    line = input()
    comma = line.index(',')
    dash1 = line.index('-', 0, comma)
    dash2 = line.index('-', comma, len(line))
    x1 = int(line[0:dash1])
    y1 = int(line[dash1 + 1 : comma])
    x2 = int(line[comma + 1 : dash2])
    y2 = int(line[dash2 + 1 : len(line)])
    print(x1, y1, x2, y2)
    
    if (x1 >= x2 and y1 <= y2):
        res += 1
    elif (x1 <= x2 and y1 >= y2):
        res += 1
        
    if (y1 < x2 or y2 < x1):
        res2 = res2
    else:
        res2 += 1

print(res, res2) # Parts 1 and 2 respectively


