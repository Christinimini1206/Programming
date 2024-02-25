"""
132
1421
18234
923

549
594
954
1443
12845
"""

lines = []
for a in range(0, 5):
    inp = str(input())
    lines.append([])
    for lst in range(0, len(inp)):
        lines[-1].append(int(inp[lst]))

for run in range(0, len(lines)):
    line = lines[run]
    # Find maximum number
    maxN, room = 0, 0
    for findMax in range(0, len(line)):
        if maxN < line[findMax]:
            maxN = line[findMax]
            room = findMax
    # Change maxN to 0 if odd
    if maxN % 2 != 0:
        line[room] = 0
    # Add 4 to maxN if even
    elif maxN % 2 == 0:
        line[room] += 4
        if line[room] >= 10:
            line[room] = str(line[room])[-1]
    # Remove 0 in the first digit
    if line[room] == 0:
        if room == 0:
            line.pop(room)
    finalStr = ''
    # Stringify the numbers
    for string in range(0, len(line)):
        finalStr += str(line[string])
    print(finalStr)