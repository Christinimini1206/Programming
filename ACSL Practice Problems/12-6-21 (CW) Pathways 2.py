"""
1,1,2,2,3,2,4,3,4,4,5,5,5,1,0,0
2,2,4,3
2,2,5,1
3,2,5,5

1,5,2,3,2,4,3,2,3,5,4,2,4,5,5,2,5,5,0,0
1,5,2,3
2,3,1,5
1,5,5,5
5,2,2,4
1,5,5,2
"""

grid = input().split(',')
l1 = input().split(',')
l2 = input().split(',')
l3 = input().split(',')
l4 = input().split(',')
l5 = input().split(',')
lines = [l1, l2, l3, l4, l5]

for a in range(0, len(grid)):
    grid[a] = int(grid[a])
for a in range(0, len(lines)):
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

gridP = []
for a in range(0, len(grid)):
    if (a + 1) % 2 == 0:
        gridP.append([])
        for b in range(a - 1, a + 1):
            gridP[-1].append(grid[b])
gridP.pop()

linesP = []
for a in range(0, len(lines)):
    linesP.append([])
    for b in range(0, len(lines[a])):
        if (b + 1) % 2 == 0:
            linesP[a].append([])
            for c in range(b - 1, b + 1):
                linesP[a][-1].append(lines[a][c])

'''
0 0 0 0 1
0 0 1 1 0
0 1 0 0 1
0 1 0 0 1
0 1 0 0 1

[1, 1] [1, 2] [1, 3] [1, 4] x
[2, 1] [2, 2] x      x      [2, 5]
[3, 1] x      [3, 3] [3, 4] x
[4, 1] x      [4, 3] [4, 4] x
[5, 1] x      [5, 3] [5, 4] x
'''

for a in range(0, len(linesP)):
    line = linesP[a]
    start, end, position = line[0], line[1], line[0]
    startX, startY = start[0], start[1]
    endX, endY = end[0], end[1]
    posX, posY = position[0], position[1]
    #while position != end:
    possibleWays = []
    print(position)

    for b in range(0, len(gridP)):
        if gridP[b] != start and gridP[b] != end:
            # Left and Right
            if abs(posX - gridP[b][0]) == 1:
                possibleWays.append(gridP[b])
                print(possibleWays, 1)

            # Up and Down
            elif abs(posY - gridP[b][1]) == 1:
                possibleWays.append(gridP[b])
                print(possibleWays, 2, posY, gridP[b][1])

            # Diagonally
            elif abs(posX - gridP[b][0]) == 1 and abs(posY - gridP[b][1]) == 1:
                possibleWays.append(gridP[b])
                print(possibleWays, 3)

            else:
                print(possibleWays)

    print('')
