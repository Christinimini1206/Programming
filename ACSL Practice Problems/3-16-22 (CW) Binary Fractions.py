"""
3, 10
1, 4
3, 5
5, 8
33, 25

3, 4
5, 12
4, 50
7, 9
38, 5
"""

lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for run in range(0, len(lines)):
    line = lines[run]
    num = line[0] / line[1]
    rBin = bin(int(str(num)[0]))[2:] + '.'
    if num >= 1:
        while num >= 1:
            num -= 1
    # Calculate
    for divide in range(0, 6):
        num *= 2
        rBin += str(num)[0]
        if num >= 1:
            num -= 1
        '''if num >= 1:
            while num >= 1:
                num -= 1
        num *= 2
        rBin += str(num)[0]
        if num >= 1:
            while num >= 1:
                num -= 1'''
    # Calculate the number with bin number
    pt = rBin.index('.')
    fNum = int(rBin[:pt], 2)
    power = 1
    for numbers in range(pt + 1, len(rBin)):
        fNum += int(rBin[numbers]) * (1/(2 ** power))
        power += 1
    fNum = str(fNum)
    while len(fNum) != 8:
        fNum += '0'
        if len(fNum) == 8:
            break
    print(str(rBin) + ', ' + str(fNum))

