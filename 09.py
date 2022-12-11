import random
import sys
import math
import collections

n = int(input())

cycles = 0
signal = 1

res = 0

protogen = []
row = ""

def draw(x, cycle):
    global row
    if (cycle % 40 == 0):
        protogen.append(row)
        row = ""
    
    if (abs((cycle % 40) - x) < 2):
        row = row + "#"
    else:
        row = row + "."
    

for i in range(n):
    line = input()
    if (line[0:4] == "noop"):
        cycles += 1
        draw(signal, cycles - 1)
        if (cycles % 40 == 20):
            res += cycles * signal
        continue
    
    val = int(line[5:])
    cycles += 1
    if (cycles % 40 == 20):
        res += cycles * signal
    draw(signal, cycles - 1)
    cycles += 1
    if (cycles % 40 == 20):
        res += cycles * signal
    draw(signal, cycles - 1)
    signal += val
    
protogen.append(row)

print(res)

for i in range(len(protogen)):
    print(protogen[i])
   
