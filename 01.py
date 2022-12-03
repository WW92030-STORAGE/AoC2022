import random
import sys
import math
import collections

def devop(c):
    if ((c == 'A') or (c == 'X')):
        return 1
    elif ((c == 'B') or (c == 'Y')):
        return 2
    return 3
    
def vs(a, b):
    dx = (a - b + 300) % 3
    if (dx == 1):
        return 6
    elif (dx == 0):
        return 3
    return 0

n = int(input())
print(n)

# PART ONE

'''
score = 0
for i in range(n):
    string = input()
    opp = devop(string[0])
    you = devop(string[2])
    
    score += you
    score += vs(you, opp)

print(score)
'''

# PART TWO

def solve(opp, ins):
    res = 0
    if (ins == 'X'):
        res = (opp + 5) % 3
    elif (ins == 'Y'):
        res = opp
    else:
        res = (opp + 7) % 3
    if (res == 0):
        res = 3
    return res
    
    

score = 0
for i in range(n):
    string = input()
    opp = devop(string[0])
    you = solve(opp, string[2])
    
    print(opp, string[2], you)
    
    score += you
    score += vs(you, opp)
print(score)
