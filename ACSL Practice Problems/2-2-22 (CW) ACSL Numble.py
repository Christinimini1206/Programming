"""
9678415, 7
9678415, 6
9678415, 5
9678415, 4
2678515, 3

4361842, 7
9143675, 6
1473518, 5
8264123, 4
7439264, 3
"""

'''def appendStr(lst, empLst, num):
    for group3 in range(0, num):
        empLst.append(lst[group3])
    return empLst'''


def removeN(lst1, setOfN):
    for a in range(0, len(setOfN)):
        lst1[setOfN[a]] = ''
    return lst1


def addStr(lst1):
    string = ''
    lst1 = lst1[::-1]
    for a in range(0, len(lst1)):
        if lst1[a] != '':
            string += str(lst1[a])
    return string


lines = []
for a in range(0, 1):
    lines.append(input().split(', '))

for run in range(0, len(lines)):
    line = lines[run]
    tile, length = line[0], int(line[1])
    tileSpl = []
    for spl in range(0, len(tile)):
        tileSpl.append(int(tile[spl]))
    tileSpl.sort()
    '''stay, move = 0, length
    add = 0
    for group in range(0, len(tileSpl)):
        for group2 in range(0, len(tileSpl)):
            numbers = []
            for group3 in range(stay, move):
                if stay - move == 6 and move <= length:
                    numbers.append(tileSpl[group3])

            stay += 1
            move += 1
            # splitNum = appendStr(tileSpl, numbers, length)

            print(numbers)
        add += 1'''

    # Add all the numbers
    sums = 0
    for add in range(0, len(tileSpl)):
        sums += tileSpl[add]

    printed = ''
    if length == len(tileSpl):  # When length = 7
        if sums % 5 == 0:
            printed = addStr(tileSpl)
    if length == 6:  # When length = 6
        for sub1 in range(0, len(tileSpl)):
            if (sums - tileSpl[sub1]) % 5 == 0:
                tileSpl.pop(sub1)
                printed = addStr(tileSpl)
                break
    if length == 5:  # When length = 5
        for sub2 in range(0, len(tileSpl)):
            for sub2_1 in range(1, len(tileSpl)):
                setLst = [sub2, sub2_1]
                setN = tileSpl[sub2] + tileSpl[sub2_1]
                # print(tileSpl, tileSpl[sub2], tileSpl[sub2_1], setLst)
                if (sums - setN) % 5 == 0:
                    printed = addStr(removeN(tileSpl, setLst))
                    break
            break
    if length == 4:
        for sub3 in range(0, len(tileSpl)):
            for sub3_1 in range(1, len(tileSpl)):
                for sub3_2 in range(2, len(tileSpl)):
                    setLst2 = [sub3, sub3_1, sub3_2]
                    setN = tileSpl[sub3] + tileSpl[sub3_1] + tileSpl[sub3_2]
                    # print(tileSpl, tileSpl[sub3], tileSpl[sub3_1], tileSpl[sub3_2])
                    if (sums - setN) % 5 == 0:
                        printed = addStr(removeN(tileSpl, setLst2))
                        break
                break
            break
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
            break
    # Prints the final output
    if printed == '':
        print('NONE')
    else:
        print(printed)
    '''else:  # When length != len(tileSpl)
        # Subtract the numbers from tile
        numAdd = len(tileSpl)
        nums = []
        for pos in range(0, len(tileSpl)):
            posC = pos + 1
            while numAdd != 0:
                for group in range(posC, len(tileSpl)):
                    partG = []
                    if tileSpl[pos] != tileSpl[group]:
                        partG.append(tileSpl[pos])
                        partG.append(tileSpl[group])
                        # print(tileSpl[pos], tileSpl[group])
                        nums.append(partG)
                        # print(nums, numAdd)
                        subN = 0
                        print(nums)
                        for addN in range(0, len(partG)):
                            subN += partG[addN]
                        if (sums - subN) % 5 == 0:
                            for pop in range(0, len(nums)):
                                tileSpl.pop()
                            print(addStr(tileSpl), 'asdf')

                pos += 1
                numAdd -= 1'''

'''
        for sub in range(0, len(tileSpl)):
            if (sums - subN) % 5 == 0:
                tileSpl.pop(sub)
                print(addStr(tileSpl))
                break
'''