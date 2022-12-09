import random
import sys
import math
import collections

n = int(input())

grid = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    line = input()
    for j in range(n):
        grid[i][j] = ord(line[j]) - ord('0')

for i in range(n):
    continue
    print(grid[i])
    
res = 0
for i in range(n):
    for j in range(n):
        good1 = True
        good2 = True
        good3 = True
        good4 = True
        tester = grid[i][j]
        for k in range(0, i):
            good1 = good1 and (grid[k][j] < tester)
        for k in range(i + 1, n):
            good2 = good2 and (grid[k][j] < tester)
        for k in range(0, j):
            good3 = good3 and (grid[i][k] < tester)
        for k in range(j + 1, n):
            good4 = good4 and (grid[i][k] < tester)
        
        if (good1 or good2 or good3 or good4):
            res += 1

print(res)

res = 0

for i in range(n):
    for j in range(n):
        d1 = 0
        d2 = 0
        d3 = 0
        d4 = 0
        tester = grid[i][j]
        for k in range(i - 1, -1, -1):
            d1 += 1
            if (grid[k][j] >= tester):
                break
            
        for k in range(i + 1, n):
            d2 += 1
            if (grid[k][j] >= tester):
                break
            
        for k in range(j - 1, -1, -1):
            d3 += 1
            if (grid[i][k] >= tester):
                break
            
        for k in range(j + 1, n):
            d4 += 1
            if (grid[i][k] >= tester):
                break
            
        # print(i, j, tester, d1, d2, d3, d4)
        
        res = max(res, d1 * d2 * d3 * d4)

print(res)
