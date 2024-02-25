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
lines = []

for a in range(0, 5):
    lines.append(input().split(','))

for a in range(0, len(lines)):
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

gridPairs = []
for a in range(0, len(grid)):
    if a % 2 == 0:
        gridPairs.append([])
        for b in range(a, a + 2):
            gridPairs[-1].append(int(grid[b]))

linePairs = []
for a in range(0, len(lines)):
    linePairs.append([])
    for b in range(0, len(lines[a])):
        if b % 2 == 0:
            linePairs[-1].append([])
            for c in range(b, b + 2):
                linePairs[-1][-1].append(lines[a][c])

'''
[1, 1] [1, 2] [1, 3] [1, 4] x
[2, 1] [2, 2] x      x      [2, 5]
[3, 1] x      [3, 3] [3, 4] x
[4, 1] x      [4, 3] [4, 4] x
[5, 1] x      [5, 3] [5, 4] x
'''

gridPairs.pop()
print(linePairs)
for a in range(0, len(linePairs)):
    gridPairsC = gridPairs.copy()
    pairs = linePairs[a]
    start, end = pairs[0], pairs[1]
    startX, startY = start[0], start[1]
    endX, endY = end[0], end[1]
    # Find the direction (left/right)
    if endX - startX > 0:  # End point is on the right
        for b in range(0, len(gridPairsC)):
            if gridPairsC[b][0] < startX:
                gridPairsC[b] = ''
    elif endX - startX < 0:  # End point is on the left
        for b in range(0, len(gridPairsC)):
            if gridPairsC[b][0] > startX:
                gridPairsC[b] = ''

    newGrid = []
    for b in range(0, len(gridPairsC)):
        if gridPairsC[b] != '':
            newGrid.append(gridPairsC[b])

    # Find the direction (up/down)
    if endY - startY > 0:  # End point is higher
        for b in range(0, len(newGrid)):
            print(newGrid[b][1], startY)
            if newGrid[b][1] < startY:
                newGrid[b][1] = ''
                print('asdf')
    elif endY - startY < 0:  # End point is lower
        for b in range(0, len(newGrid)):
            if newGrid[b][1] > startY:
                newGrid[b][1] = ''
                print('lkj')
    print(newGrid)

    '''
    pairs = linePairs[a]
    start, end = pairs[0], pairs[1]
    way = []
    way.append(start)
    # Check for the first way
    for b in range(0, len(gridPairs)):
        pair = gridPairs[b]
        if abs(gridPairs[b][0] - start[0]) == 1 or abs(gridPairs[b][1] - start[1]) == 1:
            way.append(pair)
    '''
