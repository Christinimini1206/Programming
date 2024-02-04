import math
from itertools import combinations


"""
4
on 1 2
none 10 14
none 11 15
off 2 3
"""


def calculateInitialAndFinal(none, onOff, totalOnOff, prevInitial, prevFinal):
    initialCalc = [none[0] - onOff[0][1] + onOff[1][0], none[1] - onOff[0][0] + onOff[1][1]]
    if initialCalc[0] > prevInitial[0]:
        prevInitial[0] = initialCalc[0]
    if initialCalc[1] < prevInitial[1]:
        prevInitial[1] = initialCalc[1]

    corrected_total_off_set = [[totalOnOff[i][j] - onOff[i][j] for j in range(2)] for i in range(2)]
    finalCalc = [none[0] + corrected_total_off_set[0][0] - corrected_total_off_set[1][1],
                 none[1] + corrected_total_off_set[0][1] - corrected_total_off_set[1][0]]
    if finalCalc[0] > prevFinal[0]:
        prevFinal[0] = finalCalc[0]
    if finalCalc[1] < prevFinal[1]:
        prevFinal[1] = finalCalc[1]
    # print([[(i, j) for j in range(2)] for i in range(2)])

    prevInitial[0] = 0 if prevInitial[0] < 0 else prevInitial[0]
    prevInitial[1] = 0 if prevInitial[1] < 0 else prevInitial[1]
    prevFinal[0] = 0 if prevFinal[0] < 0 else prevFinal[0]
    prevFinal[1] = 0 if prevFinal[1] < 0 else prevFinal[1]
    return prevInitial, prevFinal


'''Input'''
N = int(input())
lines = []
for i in range(N):
    lines.append(input().split())
    for ch in range(1, len(lines[i])):
        lines[i][ch] = int(lines[i][ch])

initial = [0, 1000000000000]
final = [0, 1000000000000]
offset = [[0, 0], [0, 0]]
totalOffSet = [[0, 0], [0, 0]]
for line in lines:
    # If not "none", gather all the items
    if line[0] == 'on':
        totalOffSet[0][0] += line[1]
        totalOffSet[0][1] += line[2]
    elif line[0] == 'off':
        totalOffSet[1][0] += line[1]
        totalOffSet[1][1] += line[2]

for line in lines:
    # If not "none", gather all the items
    if line[0] == 'on':
        offset[0][0] += line[1]
        offset[0][1] += line[2]
    elif line[0] == 'off':
        offset[1][0] += line[1]
        offset[1][1] += line[2]
    else:
        initial, final = calculateInitialAndFinal(line[1:], offset, totalOffSet, initial, final)

    # If "none," go until it reaches the end of the "none block"
        # Find the common range and calculate with the whole
print(f'{initial[0]} {initial[1]}')
print(f'{final[0]} {final[1]}')


"""
'''Get highways'''

# Method 1
highway = []
for l in range(len(lines)):
    if lines[l][0] == 'none':
        highway.append(lines[l][1])
        highway.append(lines[l][2])
'''
highway.sort()
markRange = [highway[math.ceil((len(highway)) / 2) - 1], highway[math.ceil((len(highway)) / 2)]]
print(markRange)
'''
# Method 2
detRange = [0] * max(highway)
print(detRange)
for l in range(len(lines)):
    highway = []
    if lines[l][0] == 'none':
        highway.append(lines[l][1])
        highway.append(lines[l][2])
        for ad in range(highway[0], highway[1] + 1):
            detRange[ad - 1] += 1
print(detRange)

markRange = []
for r in range(len(detRange)):
    if (detRange[r] == 2 and detRange[r - 1] != 2) or (detRange[r] == 2 and detRange[r + 1] != 2):
        markRange.append(r + 1)
print(markRange)

'''Calculate before mile 1'''
on = []
for a in range(len(lines)):
    if lines[a][0] == 'on':
        on.append(lines[a][1:])

for c in on:
    start, end = c[0], c[1]
    onRange = [start, end]
    differ = list(combinations(onRange, 2))
    for cc in range(len(differ)):
        markRange[0] -= differ[cc][0]
        markRange[1] -= differ[cc][1]
print(f'{markRange[0]} {markRange[1]}')

'''Calculate after mile N'''
"""