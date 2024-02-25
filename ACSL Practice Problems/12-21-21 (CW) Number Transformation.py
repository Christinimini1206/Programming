"""
296351 5
762184 3
45873216 7
19750418 6
386257914 5
"""

lines = []
for a in range(0, 5):
    lines.append(input().split(' '))
    for b in range(1, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for a in range(0, len(lines)):
    line = lines[a]
    swapN = line[0]
    P = line[1]

    swapN = swapN[::-1]
    number = int(swapN[P - 1])

    reswapN = swapN[::-1]
    roomN = (len(reswapN) - P)

    lst = []
    for b in range(0, len(reswapN)):
        lst.append(int(reswapN[b]))

    newLst = []
    for b in range(0, len(reswapN)):
        numberLst = int(reswapN[b])
        # Numbers in front of P
        if b < roomN:
            numberLst += number
            if numberLst >= 10:
                numberLst = str(numberLst)
                numberLst = numberLst[-1]
            finalN = str(numberLst)
            newLst.append(finalN)
        # P
        elif b == roomN:
            finalN = str(numberLst)
            newLst.append(finalN)
        # Numbers behind of P
        elif b > roomN:
            finalN = str(abs(numberLst - number))
            newLst.append(finalN)

    finalStr = ''
    for b in range(0, len(newLst)):
        finalStr += newLst[b]
    print(finalStr)
    """newStr = []
    N = line[0]
    digit = int(swapN[line[1] - 1])
    print(digit)
    for b in range(0, len(N)):
        if int(N[b]) < digit:
            add = str(int(N[b]) + digit)
            add = add[-1]
            newStr.append(add)
            print(b + 1, line[1] - 1)
        '''elif b == line[1] - 1:
            newStr.append(N[b])
            print('pppp')
        elif b > line[1] - 1:
            differ = abs(int(N[b]) - digit)
            newStr.append(differ)
            print('lkjh')'''
    print(newStr)"""


