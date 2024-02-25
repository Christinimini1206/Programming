"""
AAAABBBBAACCCCCCDDDDDDD
XXXXXXXXXXXXYYYYZZZZZZZZZZZZ
RSRSRSRRRRRRRRSSSSSSSSSSSSSST
WWWWWWBBBWWWWWWWWWBBBBWWW

AAAAAABBBB
AABBCCDDDDA
CCCCCCCDDDDDCCC
ABCDDDDCCCCCC
AAAAEAAAAAEEAAAAAAE
"""


def removeString(lst, str1):
    for a in range(0, len(str1)):
        lst.pop(0)
    return lst


l1 = input()
l2 = input()
l3 = input()
l4 = input()
lines = [l1, l2, l3, l4]

for a in range(0, len(lines)):
    string = lines[a]
    letters = ['']
    for b in range(0, len(string)):
        if letters[-1] != string[b]:
            if '' in letters:
                letters.pop(0)
            letters.append(string[b])

    dString = []
    for b in range(0, len(string)):
        dString.append(string[b])

    divided = []
    for b in range(0, len(letters)):
        pString = ''
        for c in range(0, len(dString)):
            if letters[b] == dString[c]:
                pString += dString[c]
            else:
                divided.append(pString)
                removeString(dString, pString)
                break

    pString = ''
    for b in range(0, len(dString)):
        pString += dString[b]
    divided.append(pString)

    finalStr = ''
    for b in range(0, len(divided)):
        com = str(len(divided[b])) + divided[b][0]
        finalStr += com
    print(finalStr)

