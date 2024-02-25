"""
4, 1, 8, 2, 8, 6, 3, 6, 6
7, 1, 7, 2, 7, 3, 8, 5, 3, 7, 3, 6, 5, 6, 7
7, 3
6, 5
5, 3
3, 8
1, 7

4, 1, 1, 2, 2, 2, 6, 1, 7
9, 2, 1, 1, 2, 3, 2, 1, 5, 2, 5, 2, 3, 1, 6, 2, 7, 1, 8
2, 1
1, 2
1, 5
1, 8
2, 7
"""

# Input
ptsO = input().split(', ')
ptsX = input().split(', ')
# List of X that will capture O
capX = []
for a in range(0, 5):
    capX.append(input().split(', '))
    for b in range(0, len(capX[a])):
        capX[a][b] = int(capX[a][b])
pts = [ptsO, ptsX]
# Convert the numbers to integers
for a in range(0, len(pts)):
    for b in range(0, len(pts[a])):
        pts[a][b] = int(pts[a][b])
# Divide the numbers into ordered pairs
ptsDiv = [[], []]
for p in range(0, len(pts)):
    for pt in range(1, len(pts[p])):
        if pt % 2 != 0:
            ptsDiv[p].append([])
            ptsDiv[p][-1].append(pts[p][pt])
        else:
            ptsDiv[p][-1].append(pts[p][pt])

ptsO, ptsX = ptsDiv[0], ptsDiv[1]

# Run the code
for run in range(0, len(capX)):
    ptCheck = capX[run]
    x, y = ptCheck[0], ptCheck[1]
    # Check if there is O on left, right, up, and down
    ptO, pos = [], []  # O that is next to the X
    if [x + 1, y] in ptsO:
        ptO.append([x + 1, y])
        pos.append('H')
    if [x - 1, y] in ptsO:
        ptO.append([x - 1, y])
        pos.append('H')
    if [x, y + 1] in ptsO:
        ptO.append([x, y + 1])
        pos.append('V')
    if [x, y - 1] in ptsO:
        ptO.append([x, y - 1])
        pos.append('V')

    # Check if any other X is placed horizontally or vertically
    possiblePts = []
    if ptO == []:  # If there are no O's
        print('NONE')
    else:
        for check in range(0, len(ptO)):
            none = 0
            xO, yO = ptO[check][0], ptO[check][1]
            final = str(xO) + ', ' + str(yO)
            if pos[check] == 'H':  # Horizontally
                if xO > x:  # If O is on the left
                    if [xO + 1, y] in ptsX:
                        print(final)
                        break
                    else:
                        none += 1
                        if len(ptO) == 1:
                            break
                elif xO < x:  # If O is on the right
                    if [xO - 1, y] in ptsX:
                        print(final)
                        break
                    else:
                        none += 1
                        if len(ptO) == 1:
                            break
            else:  # Vertically
                if yO > y:  # If O is above
                    if [x, yO + 1] in ptsX:
                        print(final)
                        break
                    else:
                        none += 1
                        if len(ptO) == 1:
                            break
                elif yO < y:  # If O is below
                    if [x, yO - 1] in ptsX:
                        print(final)
                        break
                    else:
                        none += 1
                        if len(ptO) == 1:
                            break
        if none >= 1:
            print('NONE')
