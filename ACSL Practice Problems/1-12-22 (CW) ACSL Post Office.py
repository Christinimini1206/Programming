"""
4, 4, .009
5, 7, .013
5, 7, .2
10, 12, .4
10, 12, 30

5, 8, .011
7, 10, .18
8.5, 11, .36
20, 20, 40
10, 20, 30
"""

lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        if '.' in lines[a][b]:
            lines[a][b] = float(lines[a][b])
        else:
            lines[a][b] = int(lines[a][b])

for a in range(0, len(lines)):
    line = lines[a]
    length, width, thick = line[0], line[1], line[2]
    typeM, typeOfP = [], ''
    # Regular PC
    if 3.5 <= length <= 4.25:
        if 3.5 <= width <= 6:
            if 0.007 <= thick <= 0.016:
                if typeOfP == '':
                    typeOfP = 'regular post card'
    # Large PC
    if 4.25 <= length <= 6:
        if 6 <= width <= 11.5:
            if 0.007 <= thick <= 0.16:
                if typeOfP == '':
                    typeOfP = 'large post card'
    # Envelope
    if 3.5 <= length <= 6.125:
        if 5 <= width <= 11.5:
            if 0.016 <= thick <= 0.25:
                if typeOfP == '':
                    typeOfP = 'envelope'
    # Large Envelope
    if 6.125 <= length <= 24:
        if 11 <= width <= 18:
            if 0.25 <= thick <= 0.5:
                if typeOfP == '':
                    typeOfP = 'large envelope'
    # Package
    distance = 2 * (length + thick) + length
    if not 6.125 <= length <= 24:
        if not 11 <= width <= 18:
            if not 0.25 <= thick <= 0.5:
                if distance <= 84:
                    if typeOfP == '':
                        typeOfP = 'package'
     # Large Package
    if 84 < distance <= 130:
        if typeOfP == '':
            typeOfP = 'large package'
    # Else:
    else:
        if typeOfP == '':
            typeOfP = 'unmailable'
    print(typeOfP)
