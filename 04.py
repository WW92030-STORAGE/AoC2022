import random
import sys
import math
import collections

cols = int(input())
rows = int(input())
lines = int(input())

list = [[' ' for i in range(rows * cols)] for j in range(cols)]
initial = []

for row in range(rows):
    initial.append(input())
    
heights = [0 for i in range(cols)]

print(initial)

for i in range(rows):
    row = rows - i - 1
    for j in range(cols):
        c = initial[row][4 * j + 1]
        list[j][i] = c
        
input()

for i in range(cols):
    for j in range(rows):
        if (list[i][j] != ' '):
            heights[i] = max(heights[i], j)
        print(list[i][j], end = "")
    print()

input()

print(heights)

# PART ONE

'''
for sk in range(lines):
    line = input()
    if (line[6] != ' '):
        n = int(line[5:7])
        s = int(line[1 + 4 + 1 + 1 + 4 + 1 + 1]) - 1
        e = int(line[1 + 4 + 1 + 1 + 4 + 1 + 1 + 1 + 2 + 1 + 1]) - 1
    else:
        n = int(line[5])
        s = int(line[4 + 1 + 1 + 4 + 1 + 1]) - 1
        e = int(line[4 + 1 + 1 + 4 + 1 + 1 + 1 + 2 + 1 + 1]) - 1
    print(n, s, e)
    
    for i in range(n):
        tobemoved = list[s][heights[s]]
        heights[s] -= 1
        heights[e] += 1
        list[e][heights[e]] = tobemoved
'''

# PART TWO

for sk in range(lines):
    line = input()
    if (line[6] != ' '):
        n = int(line[5:7])
        s = int(line[1 + 4 + 1 + 1 + 4 + 1 + 1]) - 1
        e = int(line[1 + 4 + 1 + 1 + 4 + 1 + 1 + 1 + 2 + 1 + 1]) - 1
    else:
        n = int(line[5])
        s = int(line[4 + 1 + 1 + 4 + 1 + 1]) - 1
        e = int(line[4 + 1 + 1 + 4 + 1 + 1 + 1 + 2 + 1 + 1]) - 1
    print(n, s, e)
    
    stack = [' '] * n
    
    for i in range(n):
        stack[i] = list[s][heights[s]]
        heights[s] -= 1
    
    for i in range(n):
        heights[e] += 1
        list[e][heights[e]] = stack[n - i - 1]

for i in range(cols):
    print(list[i][heights[i]], end="")

