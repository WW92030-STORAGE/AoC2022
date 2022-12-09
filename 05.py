import random
import sys
import math
import collections

line = input()
n = len(line)

# PART ONE

for i in range(n - 4):
    c1 = line[i]
    c2 = line[i + 1]
    c3 = line[i + 2]
    c4 = line[i + 3]
    
    s = set()
    s.update([c1, c2, c3, c4])
    # print(s)
    if (len(s) == 4):
        print(i + 4)
        break
    
# PART TWO

for i in range(n - 14):
    
    s = set()
    for j in range(14):
        s.update(line[i + j])
    # print(s)
    if (len(s) == 14):
        print(i + 14)
        break
