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

lines = []
for a in range(0, 5):
    lines.append(input().split(', '))

for run in range(0, len(lines)):
    operate, string = lines[run][0], lines[run][1]
    if operate == 'DIVIDE':
        str1, str2 = string[0:4] * 2, string[4:8] * 2
        print(str1, 'and', str2)
    elif 'ADD' in operate:
        num = int(operate[-1])
        strAdd = string[0:num] * 2
        lenRemain = len(string) - len(strAdd)
        plus = string[num:num + lenRemain]
        print(strAdd + plus)
    elif 'SUBTRACT' in operate:
        num2 = int(operate[-1])
        strSub = string[num2:]
        lenRemain2 = len(string) - len(strSub)
        plus2 = string[len(string) - lenRemain2:]
        print(strSub + plus2)