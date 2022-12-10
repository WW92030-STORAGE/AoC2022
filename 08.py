import random
import sys
import math
import collections

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def direction(x):
    if (x == 'U'):
        return 1
    elif (x == 'L'):
        return 2
    elif (x == 'D'):
        return 3
    return 0

def update(pii, d):
    x = pii[0] + dx[d % 4]
    y = pii[1] + dy[d % 4]
    return (x, y)

def movement(head, tail): # Update movement
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if (dx == 2 and abs(dy) < 2):
        return (head[0] - 1, head[1])
    elif (dx == -2 and abs(dy) < 2):
        return (head[0] + 1, head[1])
    elif (dy == 2 and abs(dx) < 2):
        return (head[0], head[1] - 1)
    elif (dy == -2 and abs(dx) < 2):
        return (head[0], head[1] + 1)
    elif (dx == 2 and dy == 2):
        return (head[0] - 1, head[1] - 1)
    elif (dx == -2 and dy == 2):
        return (head[0] + 1, head[1] - 1)
    elif (dx == 2 and dy == -2):
        return (head[0] - 1, head[1] + 1)
    elif (dx == -2 and dy == -2):
        return (head[0] + 1, head[1] + 1)
    return (tail[0], tail[1])

vis = set()

n = int(input())

head = (0, 0)
tail = (0, 0)

'''
for index in range(n):
    line = input()
    
    dir = direction(line[0])
    steps = int(line[2:])
    
    for i in range(steps):
        vis.add(tail)
        head = update(head, dir)
        
        tail = movement(head, tail)
        vis.add(tail)
        # print(head, tail)
'''

# PART TWO

rope = [(0, 0) for i in range(10)]
for index in range(n):
    line = input()
    
    dir = direction(line[0])
    steps = int(line[2:])
    
    for i in range(steps):
        vis.add(rope[9])
        rope[0] = update(rope[0], dir)
        
        for j in range(9):
            rope[j + 1] = movement(rope[j], rope[j + 1])
        vis.add(rope[9])
        # print(head, tail)

print(len(vis))
print(vis)

