"""
3, 1, A, 3, C, 8, A
3, 1, A, 6, C, 8, B
3, 1, B, 6, B, 9, C
2, 1, C, 5, B
2, 3, B, 7, A

4, 1, A, 2, B, 8, A. 9, B
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


def checkBlank(dSet1):
    for check in range(0, len(dSet1)):
        for check1 in range(0, len(dSet1[check])):
            lst = dSet1[check][check1]
            countN, lstN = 0, []
            for checkN in range(0, len(lst)):
                if ord('1') <= ord(lst[checkN]) <= ord('9'):
                    countN += 1
                    lstN.append(lst[checkN])
            if countN == 1:
                for checkL in range(0, len(letters)):
                    if letters[checkL] not in lst:
                        for repl in range(0, len(lstN)):
                            lst[int(lstN[repl]) - 1] = letters[checkL]
                        # dSet1[1][check][checkL] = letters[room]
                    print(lst[check])
    return dSet1


def checkBlankReverse(dSet1):
    for check in range(0, len(dSet1)):
        for check1 in range(0, len(dSet1[check])):
            lst = dSet1[check][check1]
            if lst.count('') == 1:
                for checkL in range(0, len(letters)):
                    if letters[checkL] not in lst:
                        room = lst.index('')
                        lst[room] = letters[checkL]
                        dSet1[1][check][checkL] = letters[room]
                    print(lst[check])
    return dSet1


lines = []
# Input
for a in range(0, 1):
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

    # Replace 'number' with letters with points
    for rPts in range(0, len(pts)):
        point = pts[rPts]
        grid[point[0] - 1] = point[1]

    dGridR = divideGridR(grid)  # Divide grid into 3 rows
    dGridC = divideGridC(grid)  # Divide grid into 3 columns
    # dGridD = divideGridD(grid)  # Get 2 diagonal lines from the grid
    divideSet = [dGridR, dGridC]

    # Check if it's possible to put any letters
    letters = ['A', 'B', 'C']
    cGrid = checkBlank(divideSet)

    # Make a set of numbers with letters
    lstNumLet = [['1'], ['2'], ['3']]
    for group in range(0, len(lstNumLet)):
        lstNumLet[group].append(cGrid[0][0][group])

    # Replace numbers with letters

    cGrid = checkBlank(cGrid)
    '''
    [['A', '', 'C'], ['', '', ''], ['', 'A', '']]
    [['A', '', ''], ['', '', 'A'], ['C', '', '']]
    [['A', '', ''], ['C', '', '']]
    
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    [[1, 5, 9], [3, 5, 7]]
    '''

    print(cGrid)

