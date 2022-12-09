import random
import sys
import math
import collections

n = int(input())

cur = ""

pars = {} # Parent directory
dirs = {} # Nested directories
sizes = {} # Directory sizes

dirs[""] = []
sizes[""] = 0
pars[""] = ""

alldirs = set()
alldirs.add("")

stack = [""]

def stackstring(stack):
    res = ""
    for i in range(len(stack)):
        res = res + str(stack[i]) + "|"
    return res[0:len(res) - 1]

def size(dirs, sizes, src):
    res = 0
    if (src in sizes.keys()):
        res += sizes[src]
    for d in dirs[src]:
        res += size(dirs, sizes, d)
    return res

for i in range(n):
    line = input()
    if (line[0] == '$'):
        if (line[2:4] == "cd"):
            if (line[5] == '/'):
                cur == ""
            elif (line[5:7] == ".."):
                del stack[len(stack) - 1]
                cur = stackstring(stack)
            elif ((stackstring(stack) + "|" + line[5:]) in dirs[cur]):
                stack.append(line[5:])
                cur = stackstring(stack)
            else:
                print("ERROR " + line[5:] + " NOT FOUND") 
        elif (line[2:4] == "ls"):
            continue
    else: # File to be listed
        space = line.index(' ')
        part1 = line[0:space]
        part2 = line[space + 1:]
        print(cur, " = ", part1, part2)
        if (part1.isnumeric()):
            if (cur in sizes.keys()):
                sizes[cur] += int(part1)
            else:
                sizes[cur] = int(part1)
        elif (line[0:space] == "dir"):
            dirs[cur].append(stackstring(stack) + "|" + part2)
            pars[stackstring(stack) + "|" + part2] = cur
            dirs[stackstring(stack) + "|" + part2] = []
            sizes[stackstring(stack) + "|" + part2] = 0
            alldirs.add(stackstring(stack) + "|" + part2)
            
    # print(pars, dirs, sizes)
    
    
for d in dirs.keys():
    print("[", d, "]", dirs[d], sizes[d])
    
sum = 0
for d in dirs.keys():
    sz = size(dirs, sizes, d)
    print('[', d, ']', sz)
    if (sz <= 100000):
        sum += sz

print(sum)

minval = sys.maxsize
res = ""

total = size(dirs, sizes, "")
print(total, 70000000 - total)

for d in dirs.keys():
    sz = size(dirs, sizes, d)
    if (sz >= 30000000 - (70000000 - total)):
        if (sz < minval):
            minval = sz
            res = d

print(res, minval)

