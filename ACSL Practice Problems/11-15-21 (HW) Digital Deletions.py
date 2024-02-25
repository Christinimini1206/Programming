import time

"""
7, 3, 5, 8, 0, 2, 5, 4
6, 8, 3, 0, 7, 5, 1
5, 5, 0, 6, 0, 4

6, 1, 3, 5, 8, 6, 0
7, 2, 0, 4, 0, 1, 1, 4
8, 0, 0, 0, 5, 0, 1, 1, 3
5, 5, 2, 3, 6, 5
7, 0, 1, 3, 5, 7, 5, 2
"""

def removeZero(lst):
    while 0 in lst:
        zeroRoom = lst.index(0)
        lst = lst[zeroRoom + 1:]
    return lst


# def subtract(num):


l1 = input().split(', ')
l2 = input().split(', ')
l3 = input().split(', ')
l4 = input().split(', ')
l5 = input().split(', ')
lines = [l1, l2, l3, l4, l5]

for a in range(0, len(lines)):
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for a in range(0, len(lines)):
    line = lines[a]
    move = 0

    '''
    lineBack = line[::-1]
    newLine = []
    
    if 0 in line:
        zeroRoom = lineBack.index(0)
        for b in range(0, len(lineBack)):
            if b < zeroRoom:
                newLine.append(lineBack[b])
    '''

    if 0 in line:
        newLine = removeZero(line)
        move += 1
    else:
        newLine = line

    if len(newLine) > 0:
        while newLine != []:
            newLine = newLine[::-1]
            roomMax = newLine.index(max(newLine))
            num = max(newLine)
            if num % 2 == 0:
                num -= 2
                move += 1
            else:
                num -= 1
                move += 1
            newLine[roomMax] = num
            newLine = newLine[::-1]

            if 0 in newLine:
                while 0 in newLine:
                    zeroRoom = newLine.index(0)
                    newLine = newLine[zeroRoom + 1:]
                move += 1

    print(move)