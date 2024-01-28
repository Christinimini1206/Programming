# import time
from typing import List

"""
ID: ldoyun81
LANG: PYTHON3
TASK: skidesign
"""

'''
def checkHeights(lst):
    mini, maxi = min(lst), max(lst)
    minInd, maxInd = lst.index(mini), lst.index(maxi)
    while maxi - mini > 17:
        lst[minInd] += 1
        lst[maxInd] -= 1
        if (lst[maxInd] - lst[minInd]) <= 17:
            break
    return lst

'''


def findCost(lst, tup):
    m, M = min(lst), max(lst)
    low, up = tup[0], tup[1]
    newMin, newMax = m + low, M - up
    cost = 0
    for c in lst:
        if c < newMin:
            cost += (newMin - c) ** 2
        elif c > newMax:
            cost += (c - newMax) ** 2
    return cost


'''Input'''
fin = open("skidesign.in", 'r')
fout = open('skidesign.out', 'w')

inp = fin.read().strip().split('\n')
heights = List[int]
N, heights = int(inp[0]), list(map(int, inp[1:]))
minH, maxH = min(heights), max(heights)
gap = maxH - minH - 17

posDif = []
for d in range(0, gap + 1):
    posDif.append((d, gap - d))

cost = []
for i in posDif:
    cost.append(findCost(heights, i))

'''
# while checkHeights(heights) == False:

print(max(heights) - min(heights))

changeH = 0
indexLst = [0] * N
print(checkHeights(heights))
while max(heights) - min(heights) > 17:
    heights.sort()
    minNum = heights.count(min(heights))
    minInd, maxInd = heights.index(min(heights)), heights.index(max(heights))
    heights[0] += 1
    heights[-1] -= 1
    changeH += 1
    print(heights)
    # time.sleep(0.2)
'''



'''Output'''
fout.write(f'{min(cost)}\n')
fout.close()