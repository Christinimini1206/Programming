"""
DIVIDE, ABBCDFGG
ADD3, ABBCDFGG
SUBTRACT3, ABBCDFGG
SUBTRACT3, GGABBCDF
ADD3, GGABBCDF

DIVIDE, ABGHBEBC
ADD1, BCBCFDFD
SUBTRACT2, ABEECDAB
ADD4, ADDFHFBE
SUBTRACT0, ABCDEFGH
"""

lines = [input().split(', '),
         input().split(', '),
         input().split(', '),
         input().split(', '),
         input().split(', ')]
comb = ['DIVIDE', 'ADD', 'SUBTRACT']

for a in range(0, len(lines)):
    lineN = lines[a]
    string = lineN[1]
    # DIVIDE
    if comb[0] in lineN[0]:
        cell1, cell2 = string[0:4], string[4:8]
        cell1 += cell1
        cell2 += cell2
        print(cell1, 'and', cell2)
    # ADDn
    elif comb[1] in lineN[0]:
        num = int(lineN[0].replace('ADD', ''))
        add = string[0:num]
        addR, stringR = add[::-1], string[::-1]
        stringR += addR
        stringR = stringR[::-1]
        print(stringR[0:8])
    # SUBTRACTn
    elif comb[2] in lineN[0]:
        num = int(lineN[0].replace('SUBTRACT', ''))
        newString = string[num:]
        addS = string[8 - num:]
        newString += addS
        print(newString)