import time
"""
4

2
**
*.
1
*

3
.**
.**
***
2
.*
**

3
...
.*.
...
3
.*.
...
...

3
**.
.**
..*
2
.*
*.
"""

def convStrToN(lst):
    newLst = []
    for l in range(len(lst)):
        newLst.append([])
        for i in range(len(lst[l])):
            if lst[l][i] == '*':
                newLst[-1].append(1)
            else:
                newLst[-1].append(0)
    return newLst


# Input
T = int(input())
input()
newLines = []
for l in range(T):
    newLines.append([])
    while True:
        line = input()
        if line == '':
            break
        newLines[-1].append(line)

# Run each test case
for run in range(T):
    case = newLines[run]
    # Canvas and stamp
    canvas = case[1:int(case[0]) + 1]
    stamp = case[int(case[0]) + 2:]
    print(canvas)
    print(stamp)
    # Canvas and stamp converted to number
    canvasN, stampN = convStrToN(canvas), convStrToN(stamp)
    print("canvas", canvasN)

    # Put the stamp
    checkingArea = []
    size = [len(stampN), len(stampN[0])]
    moveDown = 0
    while True:
        moveRight = 0
        while True:
            checkingArea.append([])
            for l in range(size[0]):
                check = canvasN[l + moveDown][0 + moveRight:size[-1] + moveRight]
                checkingArea[-1].append(check)
            if len(canvasN[0]) > size[-1] + moveRight:
                moveRight += 1
            else:
                break
        print()
        if len(canvas) > l + moveDown:
            moveDown += 1
        else:
            break
    print(checkingArea)
    print('')
