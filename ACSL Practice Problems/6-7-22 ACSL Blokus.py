"""
A1, 2, 1
C1, 2, 1
G5, 2, 2
F4, 1, 2
D9, 1, 2

G6, 1, 1
G1, 2, 1
E7, 2, 1
J9, 1, 2
J1, 1, 1
"""

# Input
lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(1, len(lines[a])):
        lines[a][b] = int(lines[a][b])

# Run the code
for run in range(0, len(lines)):
    line = lines[run]
    left, right, up, down = 10, 10, 10, 10  # Tiles
    tileR, tileC = ord(line[0][0]) - 65, int(line[0][1]) - 1
    # Possible tiles (left & right)
    left, right = tileC, right - (tileC + 2)
    # Possible tiles (up & down)
    up, down = up - (tileR + 1), tileR
    # Elimination
    posPiece = ['A', 'B', 'C', 'D']
    pieceA, pieceT = line[1], line[2]
    original = [left, right, up, down]
    posCasesA = [[left, right, up, down], [left, right, up, down]]
    posCasesB = [[left, right, up, down], [left, right, up, down]]
    posCasesC = [[left, right, up, down], [left, right, up, down], [left, right, up, down]]
    posCasesD = [[left, right, up, down], [left, right, up, down], [left, right, up, down]]
    # Eliminate A
    dir = 1
    for case in range(0, 2):
        posCasesA[case][2 + dir] -= 1  # Down - 1, Up + 1
        if pieceA == 1:
            if pieceT == 2:
                posCasesA[case][0] -= 2  # Left - 2
            else:
                posPiece[0] = ''
                break
        elif pieceA == 2:
            if pieceT == 1:
                posCasesA[case][1] -= 2  # Right - 2
            else:
                posPiece[0] = ''
                break
        dir = 0
    # Eliminate B
    dir, dif = 0, 1
    for case in range(0, 2):
        if pieceA == 1:
            if pieceT == 1:
                posPiece[1] = ''
                break
            posCasesB[case][0] -= 2
            posCasesB[case][2 + dir] -= 2
        elif pieceA == 2:
            if pieceT == 2 or pieceT == 3:
                posPiece[1] = ''
                break
            posCasesB[case][1] -= 2
            posCasesB[case][2 + dir] -= dif
        dir, dif = 1, 2
    # Eliminate C
    for case in range(0, 1):
        if pieceA == 1:
            if pieceT == 2 or pieceT == 3:
                posPiece[2] = ''
                break
        elif pieceA == 2:
            if pieceT == 4 or pieceT == 3:
                posPiece[2] = ''
                break
        if pieceA == 1:
            if pieceT == 1:
                posCasesC[0][0], posCasesC[0][3] = posCasesC[0][0] - 2, posCasesC[0][3] - 2
                posCasesC[1][0], posCasesC[1][3] = posCasesC[1][0] - 3, posCasesC[1][3] - 1
            elif pieceT == 4:
                posCasesC[2][0], posCasesC[2][2] = posCasesC[2][0] - 3, posCasesC[2][2] - 2
            else:
                posPiece[2] = ''
        elif pieceA == 2:
            if pieceT == 1:
                posCasesC[0][1], posCasesC[0][3] = posCasesC[0][1] - 2, posCasesC[0][3] - 2
                posCasesC[1][1], posCasesC[1][3] = posCasesC[1][1] - 3, posCasesC[1][3] - 1
            elif pieceT == 2:
                posCasesC[2][1], posCasesC[2][2] = posCasesC[2][1] - 3, posCasesC[2][2] - 2
            else:
                posPiece[2] = ''
    # Eliminate D
    for case in range(0, 1):
        if pieceA == 1:
            if pieceT == 2:
                posPiece[2] = ''
                break
        elif pieceA == 2:
            if pieceT == 3:
                posPiece[2] = ''
                break
        if pieceA == 1:
            if pieceT == 1:
                posCasesD[0][0] -= 2
                posCasesD[0][3] -= 3
            elif pieceT == 3:
                posCasesD[1][0] -= 2
                posCasesD[1][2] -= 2
            elif pieceT == 4:
                posCasesD[2][0] -= 1
                posCasesD[2][2] -= 3
            else:
                posPiece[3] = ''
        elif pieceA == 2:
            if pieceT == 1:
                posCasesD[0][1] -= 2
                posCasesD[0][3] -= 3
            elif pieceT == 2:
                posCasesD[1][0] -= 2
                posCasesD[1][2] -= 2
            elif pieceT == 4:
                posCasesD[2][1] -= 2
                posCasesD[2][2] -= 3
            else:
                posPiece[3] = ''
    # Check negatives
    cases = [posCasesA, posCasesB, posCasesC, posCasesD]
    for a in range(0, len(cases)):
        neg = 0
        for b in range(0, len(cases[a])):
            for c in range(0, len(cases[a][b])):
                if cases[a][b][c] < 0 or cases[a][b] == original:
                    neg += 1
                    break
        if neg == len(cases[a]):
            posPiece[a] = ''
    finalStr = ''
    none = 0
    for a in range(0, len(posPiece)):
        if posPiece[a] != '':
            finalStr += posPiece[a]
            finalStr += ', '
        else:
            none += 1
    if none == 4:
        print('NONE')
    else:
        print(finalStr[0:len(finalStr) - 2])
