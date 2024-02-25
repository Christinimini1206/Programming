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

1,5,2,3,2,4,3,2,3,5,4,2,4,5,5,2,5,5,0,0
1,5,5,2

[1, 1] [1, 2] [1, 3] [1, 4] [1, 5]
[2, 1] [2, 2] [2, 3] [2, 4] [2, 5]
[3, 1] [3, 2] [3, 3] [3, 4] [3, 5]
[4, 1] [4, 2] [4, 3] [4, 4] [4, 5]
[5, 1] [5, 2] [5, 3] [5, 4] [5, 5]

[1, 1] [1, 2] [1, 3] [1, 4] [x   ]
[2, 1] [2, 2] [x   ] [x   ] [2, 5]
[3, 1] [x   ] [3, 3] [3, 4] [x   ]
[4, 1] [x   ] [4, 3] [4, 4] [x   ]
[5, 1] [x   ] [5, 3] [5, 4] [x   ]
"""

# Grid input
grid = input().split(',')
for a in range(0, len(grid)):
    grid[a] = int(grid[a])

# Other lines input
pts = []
N = 1
for a in range(0, N):
    pts.append(input().split(','))
    for b in range(0, len(pts[a])):
        pts[a][b] = int(pts[a][b])

# Dividing the numbers into points
gridPts = []
for a in range(0, len(grid)):
    if a % 2 == 0:
        gridPts.append([])
    gridPts[-1].append(grid[a])
print(gridPts)

ptsDiv = []
for a in range(0, len(pts)):
    ptsDiv.append([])
    for b in range(0, len(pts[a])):
        if b % 2 == 0:
            ptsDiv[a].append([])
        ptsDiv[a][-1].append(pts[a][b])
gridPts.pop()

for a in range(0, len(ptsDiv)):
    # print(a + 1)
    pairs = ptsDiv[a]
    start, end = pairs[0], pairs[1]
    startR, endR = gridPts.index(start), gridPts.index(end)
    indexS, indexE = 0, len(gridPts)
    startx, starty = start[0], start[1]
    endx, endy = end[0], end[1]
    found = False

    # Find all possible pathways from the starting pt
    pathway = []
    # room = gridPts.index(start)
    # roomE = gridPts.index(end)
    if startR > endR:
        for pathI in reversed(range(len(gridPts))):
            if 0 <= abs(startx - endx) <= 1:
                if 0 <= abs(starty - endy) <= 1:
                    found = True
                    break
            x, y = gridPts[pathI][0], gridPts[pathI][1]
            # print(abs(x - startx), abs(y - starty))
            if 0 <= abs(x - startx) <= 1:
                if 0 <= abs(y - starty) <= 1:
                    pathway.append(gridPts[pathI])
                    startx, starty = pathway[-1][0], pathway[-1][1]
    else:
        for pathI in range(0, len(gridPts)):
            if 0 <= abs(startx - endx) <= 1:
                if 0 <= abs(starty - endy) <= 1:
                    found = True
                    break
            x, y = gridPts[pathI][0], gridPts[pathI][1]
            # print(abs(x - startx), abs(y - starty))
            if 0 <= abs(x - startx) <= 1:
                if 0 <= abs(y - starty) <= 1:
                    pathway.append(gridPts[pathI])
                    startx, starty = pathway[-1][0], pathway[-1][1]
            # Check for the previous one
            if pathI != 0:
                xPre, yPre = gridPts[pathI - 1][0], gridPts[pathI - 1][1]
                currentPx, currentPy = gridPts[pathI]
                if 0 <= abs(xPre - currentPx) <= 1:
                    if 0 <= abs(yPre - currentPy) <= 1:
                        pathway.append(gridPts[pathI - 1])
                        currentPx, currentPy = pathway[-1][0], pathway[-1][1]
                        x, y =
    print(pathway)

    '''
    # Find pathway with other pts
    for b in range(1, len(pathway[0])):
        point = pathway[0][b]
        room2 = gridPts.index(point) - 1
        pointx, pointy = point[0], point[1]
        for c in range(room2, len(gridPts)):
            x, y = gridPts[c][0], gridPts[c][1]
            if 0 <= abs(x - pointx) <= 1:
                if 0 <= abs(y - pointy) <= 1:
                    if point != gridPts[c] and start != gridPts[c] and end != gridPts[c]:
                        pathway[0].append(gridPts[c])
    '''
    pathway.append(end)
    if found == False:
        print('NONE')
    else:
        """
        newPath = []
        for b in range(0, len(pathway[0])):
            newPath.append(pathway[0][b])
        finalLst = []
        for b in range(0, len(newPath)):
            for c in range(0, len(newPath[b])):
                finalLst.append(str(newPath[b][c]))
        finalStr = ''
        for b in range(0, len(finalLst)):
            finalStr += finalLst[b]
            if b != len(finalLst) - 1:
                finalStr += ','
        """
        print(''.join(str(elm)for elm in pathway))
        finalStr = ''
        for d in range(0, len(pathway)):
            for c in range(0, len(pathway[d])):
                if finalStr != '':
                    finalStr += ','
                finalStr += str(pathway[d][c])
        print(finalStr)



