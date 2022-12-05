import random
import sys
import math
import collections

def priority(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    
    if (c >= a and c <= z):
        return c - a + 1
    return c - A + 27

n = int(input())

sum = 0

'''

for i in range(n):
    line = input()
    length = len(line)
    part1 = line[0:(length // 2)]
    part2 = line[(length // 2):length]
    print(part1, part2)
    
    s1 = [0] * 256
    s2 = [0] * 256
    # print(len(s1))
    for index in range(length // 2):
        s1[ord(part1[index])] += 1
        s2[ord(part2[index])] += 1
    
    for val in range(256):
        if (s1[val] > 0 and s2[val] > 0):
            print(val)
            sum += priority(val)

print(sum)
'''

for i in range(n // 3):
    l1 = input()
    l2 = input()
    l3 = input()
    
    s1 = [0] * 256
    s2 = [0] * 256
    s3 = [0] * 256
    for index in range(len(l1)):
        s1[ord(l1[index])] += 1
    for index in range(len(l2)):
        s2[ord(l2[index])] += 1
    for index in range(len(l3)):
        s3[ord(l3[index])] += 1
    
    for val in range(256):
        if (s1[val] > 0 and s2[val] > 0 and s3[val] > 0):
            sum += priority(val)

print(sum)
