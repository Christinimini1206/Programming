import itertools

"""
3
MOMMOM
MMO
OOMO

8
MMM
MMO
MOM
MOO
OMM
OMO
OOM
OOO

16
MMMM
MMMO
MMOM
MMOO
MOMM
MOMO
MOOM
MOOO
OMMM
OMMO
OMOM
OMOO
OOMM
OOMO
OOOM
OOOO

32
MMMMM
MMMMO
MMMOM
MMMOO
MMOMM
MMOMO
MMOOM
MMOOO
MOMMM
MOMMO
MOMOM
MOMOO
MOOMM
MOOMO
MOOOM
MOOOO
OMMMM
OMMMO
OMMOM
OMMOO
OMOMM
OMOMO
OMOOM
OMOOO
OOMMM
OOMMO
OOMOM
OOMOO
OOOMM
OOOMO
OOOOM
OOOOO
"""

"""
1
OOMOM
"""


def findSubstring(full, sub):
    totalInd = []
    for ind in range(0, len(full) - len(sub) + 1):
        indices = []
        skip = False
        for check in range(len(sub)):
            if not sub[check] == full[ind + check]:
                skip = True
            else:
                indices.append(ind + check)
        if len(indices) == len(sub):
            totalInd.append(indices)
        if skip:
            continue
    return totalInd


'''Input'''
N = int(input())
strings = [input() for inp in range(N)]
'''
testing = list(itertools.product(['M', 'O'], repeat=5))
for l in testing:
    print(''.join(l))
'''
for string in strings:
    process = 0
    if 'MOO' == string:
        process = 0
        print(process)
        continue
    elif 'MOO' in string:
        process = len(string) - 3
        print(process)
        continue
    if 'OO' in string:
        subFound = findSubstring(string, "OO")
        if len(subFound) == 1:
            if subFound[0][0] == 0:
                process = len(string) - 1
            else:
                process = len(string) - 2
        else:
            process = len(string) - 2
    if 'MO' in string:
        subFound = findSubstring(string, "MO")
        if len(subFound) == 1:
            if subFound[0][1] == len(string) - 1 and process == 0:
                process = -1
            else:
                if process > len(string) - 2:
                    process = len(string) - 2
        else:
            if process > len(string) - 2:
                process = len(string) - 2
    else:
        process = -1
    print(process)