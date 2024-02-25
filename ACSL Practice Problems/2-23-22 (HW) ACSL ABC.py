"""
3, 1, A, 3, C, 8, A
3, 1, A, 6, C, 8, B
3, 1, B, 6, B, 9, C
2, 1, C, 5, B
2, 3, B, 7, A

4, 1, A, 2, B, 8, A, 9, B
3, 1, A, 2, B, 9, A
3, 3, C, 6, B, 7, C
2, 7, A, 6, C
2, 1, C, 6, A
"""


# Divide the grid into 3 rows
def divideGridR(lst1):
    lstSpl = []
    for a in range(0, len(lst1) - 1):
        if a % 3 == 0:
            lstSpl.append([])
            lstSpl[-1].append(lst1[a])
            lstSpl[-1].append(lst1[a + 1])
            lstSpl[-1].append(lst1[a + 2])
    return lstSpl


# Divide the grid into 3 columns
def divideGridC(lst1):
    lstSpl = []
    for a in range(0, 3):
        lstSpl.append([])
        lstSpl[-1].append(lst1[a])
        lstSpl[-1].append(lst1[a + 3])
        lstSpl[-1].append(lst1[a + 6])
    return lstSpl


# Get 2 diagonal lines from the grid
def divideGridD(lst1):
    lstSpl = []
    ptsN = [0, 2]
    add = [4, 2]
    for a in range(0, len(ptsN)):
        lstSpl.append([])
        lstSpl[-1].append(lst1[ptsN[a]])
        lstSpl[-1].append(lst1[ptsN[a] + add[a]])
        lstSpl[-1].append(lst1[ptsN[a] + add[a] * 2])
    return lstSpl


lines = []
# Input
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        if ord('1') <= ord(lines[a][b]) <= ord('9'):
            lines[a][b] = int(lines[a][b])

# Runs each line
for run in range(0, len(lines)):
    line = lines[run]
    pts, NofPts = [], line[0]
    grid = ['1', '2', '3',
            '4', '5', '6',
            '7', '8', '9']

    # Divide into separate points
    for dPts in range(1, len(line) - 1):
        if dPts % 2 != 0:
            pts.append([])
            pts[-1].append(line[dPts])
            pts[-1].append(line[dPts + 1])
    '''
    # Replace 'number' with letters with points
    for rPts in range(0, len(pts)):
        point = pts[rPts]
        grid[point[0] - 1] = point[1]
    
    dGridR = divideGridR(grid)  # Divide grid into 3 rows
    dGridC = divideGridC(grid)  # Divide grid into 3 columns
    # dGridD = divideGridD(grid)  # Get 2 diagonal lines from the grid
    divideSet = [dGridR, dGridC]
    '''

    # Possible combination sets
    posComb = [['A', 'B', 'C'],
               ['A', 'C', 'B'],
               ['B', 'A', 'C'],
               ['B', 'C', 'A'],
               ['C', 'A', 'B'],
               ['C', 'B', 'A']]
    combSet = []
    posCombSet = []
    for set1 in range(0, len(posComb)):
        posCombSet.append([])
        for set2 in range(0, len(posComb)):
            for set3 in range(0, len(posComb)):
                posCombSet = [posComb[set1], posComb[set2], posComb[set3]]
                # Eliminate the ones that cannot be possible
                counted = 0
                for checkR in range(0, len(posCombSet)):
                    if posCombSet.count(posCombSet[checkR]) > 1:
                        counted += 1
                    for elim in range(0, 2):
                        if posCombSet[0][elim] == posCombSet[1][elim] or posCombSet[0][elim] == posCombSet[2][elim] or posCombSet[1][elim] == posCombSet[2][elim]:
                            counted += 1
                if counted == 0:
                    combSet.append(posCombSet)
                    # print(posCombSet)
    # print(combSet)

    # Check if the pts match with any combination

    for sets in range(0, len(combSet)):
        # print(combSet[sets])
        accuracy = 0
        for comp in range(0, len(pts)):
            # print(combSet[sets], pts[comp])
            # print(pts[comp][1], combSet[sets][pts[comp][0]])
            if 1 <= pts[comp][0] <= 3:
                x = pts[comp][0] - 1
                # print(x + 1, pts[comp][1], combSet[sets][0][x], 'asdf', 1)
                if pts[comp][1] == combSet[sets][0][x]:
                    accuracy += 1
            elif 4 <= pts[comp][0] <= 6:
                x = pts[comp][0] - 4
                # print(x + 4, pts[comp][1], combSet[sets][1][x], 'asdf', 2)
                if pts[comp][1] == combSet[sets][1][x]:
                    accuracy += 1
            elif 7 <= pts[comp][0] <= 9:
                x = pts[comp][0] - 7
                # print(x + 7, pts[comp][1], combSet[sets][2][x], 'asdf', 3)
                if pts[comp][1] == combSet[sets][2][x]:
                    accuracy += 1
        # print(accuracy)
        if accuracy == len(pts):
            string = ''
            for a in range(0, len(combSet[sets])):
                for b in range(0, len(combSet[sets][a])):
                    string += combSet[sets][a][b]
            print(string)
            break

    # Make the list as one string

    '''
    # Subtract numbers to the pts
    for subt in range(0, len(pts)):
        if 1 <= pts[subt][0] <= 3:
            pts[subt][0] -= 1
        elif 4 <= pts[subt][0] <= 6:
            pts[subt][0] -= 4
        elif 7 <= pts[subt][0] <= 9:
            pts[subt][0] -= 7
    print(pts)'''



    """
        if length == 3:
        for sub4 in range(0, len(tileSpl)):
            for sub4_1 in range(1, len(tileSpl)):
                for sub4_2 in range(2, len(tileSpl)):
                    for sub4_3 in range(3, len(tileSpl)):
                        setLst2 = [sub4, sub4_1, sub4_2, sub4_3]
                        setN = tileSpl[sub4] + tileSpl[sub4_1] + tileSpl[sub4_2] + tileSpl[sub4_3]
                        # print(tileSpl, tileSpl[sub4], tileSpl[sub4_1], tileSpl[sub4_2], + tileSpl[sub4_3])
                        if (sums - setN) % 5 == 0:
                            printed = addStr(removeN(tileSpl, setLst2))
                            break
                    break
                break
            break"""

    '''newGrid = []
    group = 0
    for check in range(0, len(divideSet)):
        newGrid.append([])
        room = 0
        for comb in range(0, len(posComb)):
            ptsSet = divideSet[check]
            for sets in range(0, len(ptsSet)):
                ptsSetN, combSet = ptsSet[sets], posComb[comb]
                print(ptsSetN, combSet)
                occur = 0
                for checkL in range(0, len(ptsSetN)):
                    if ptsSetN[checkL] == combSet[checkL]:
                        occur += 1
                if occur >= 2:
                    ptsSetN = combSet
                newGrid[-1].append(ptsSetN)


            occur, room = 0, 0
            for checkL in range(0, 3):
                x, y = ptsSet[checkL][room], combSet[room]
                if ptsSet[group][room] == combSet[checkL]:
                    occur += 1
            room += 1
            group += 1
            if occur >= 2:
                # ptsSet[checkL] = combSet
                newGrid[-1].append(combSet)'''

