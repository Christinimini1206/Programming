"""
ATKQQJ, AKQQ, KQQJN, A
KQN, ATTQN, AQJ, ATKQJ
AAKQJNN, TN, TTKNN, KQ
TKQJ, ATKQJ, AAKQJ, JN

T, AKQJN, QJ, AATTKQJN
AQQJNN, TTKJ, TQJN, TK
TTKK, KQQNN, KKQN, KQN
AJ, AAJ, AATJ, AATQJJN
KQJJ, KQJJ, QQJJ, KQJJ
"""

# Inputs
linesStr = []
for a in range(0, 5):
    linesStr.append(input().split(', '))
# Divide the string to each letter
lines = []
for b in range(0, len(linesStr)):
    lines.append([])
    for c in range(0, len(linesStr[b])):
        lines[-1].append([])
        for d in range(0, len(linesStr[b][c])):
            lines[-1][-1].append(linesStr[b][c][d])

# Run the code
for run in range(0, len(lines)):
    line = lines[run]
    D, C, S, H = line[0], line[1], line[2], line[3]
    point = 0
    # Cases
    if D.count('J') >= 2 and S.count('Q') >= 2:  # Case 1
        dJ, sQ = D.count('J'), S.count('Q')
        while dJ > 0 and sQ > 0:
            point += 30
            dJ -= 2
            sQ -= 2
    if D.count('A') >= 1 and C.count('A') >= 1 and S.count('A') >= 1 and H.count('A') >= 1:  # Case 2
        dA, cA, sA, hA = D.count('A'), C.count('A'), S.count('A'), H.count('A')
        while dA > 0 and cA > 0 and sA > 0 and hA > 0:
            point += 10
            dA -= 1
            cA -= 1
            sA -= 1
            hA -= 1
    if D.count('K') >= 1 and C.count('K') >= 1 and S.count('K') >= 1 and H.count('K') >= 1:  # Case 3
        dK, cK, sK, hK = D.count('K'), C.count('K'), S.count('K'), H.count('K')
        while dK > 0 and cK > 0 and sK > 0 and hK > 0:
            point += 8
            dK -= 1
            cK -= 1
            sK -= 1
            hK -= 1
    if D.count('A') >= 2 and C.count('A') >= 2 and S.count('A') >= 2 and H.count('A') >= 2:  # Case 4
        dA, cA, sA, hA = D.count('A'), C.count('A'), S.count('A'), H.count('A')
        while dA > 0 and cA > 0 and sA > 0 and hA > 0:
            point += 100
            dA -= 2
            cA -= 2
            sA -= 2
            hA -= 2
    if D.count('K') >= 2 and C.count('K') >= 2 and S.count('K') >= 2 and H.count('K') >= 2:  # Case 5
        dK, cK, sK, hK = D.count('K'), C.count('K'), S.count('K'), H.count('K')
        while dK > 0 and cK > 0 and sK > 0 and hK > 0:
            point += 80
            dK -= 2
            cK -= 2
            sK -= 2
            hK -= 2
    if D.count('J') >= 1 and S.count('Q') >= 1:
        dJ, sQ = D.count('J'), S.count('Q')
        while dJ > 0 and sQ > 0:
            point += 4
            dJ -= 1
            sQ -= 1
    if D.count('Q') >= 1 and C.count('Q') >= 1 and S.count('Q') >= 1 and H.count('Q') >= 1:  # Case 3
        dK, cK, sK, hK = D.count('Q'), C.count('Q'), S.count('Q'), H.count('Q')
        while dK > 0 and cK > 0 and sK > 0 and hK > 0:
            point += 6
            dK -= 1
            cK -= 1
            sK -= 1
            hK -= 1
    if D.count('J') >= 1 and C.count('J') >= 1 and S.count('J') >= 1 and H.count('J') >= 1:  # Case 3
        dK, cK, sK, hK = D.count('J'), C.count('J'), S.count('J'), H.count('J')
        while dK > 0 and cK > 0 and sK > 0 and hK > 0:
            point += 4
            dK -= 1
            cK -= 1
            sK -= 1
            hK -= 1
    if D.count('Q') >= 2 and C.count('Q') >= 2 and S.count('Q') >= 2 and H.count('Q') >= 2:  # Case 3
        dK, cK, sK, hK = D.count('Q'), C.count('Q'), S.count('Q'), H.count('Q')
        while dK > 0 and cK > 0 and sK > 0 and hK > 0:
            point += 60
            dK -= 2
            cK -= 2
            sK -= 2
            hK -= 2
    if D.count('J') >= 2 and C.count('J') >= 2 and S.count('J') >= 2 and H.count('J') >= 2:  # Case 3
        dK, cK, sK, hK = D.count('J'), C.count('J'), S.count('J'), H.count('J')
        while dK > 0 and cK > 0 and sK > 0 and hK > 0:
            point += 40
            dK -= 2
            cK -= 2
            sK -= 2
            hK -= 2
    print(point)