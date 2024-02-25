"""
Hello world!
0, 10
1, 8
0, 5
6, 6
0, -1
-10, -2
0, -5
-4, 0

ALL-STAR CONTEST 2016
0, 10
3, 8
-8, 0
6, -6
-12, -8
"""

string = input()
lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for run in range(0, len(lines)):
    line = lines[run]
    length = len(string)
    if line[0] > 0 and line[1] > 0:
        print(string[line[0]:line[0] + line[1]])
    else:
        # When start is negative
        if line[0] < 0:
            line[0] += length
        # When length is negative
        if line[1] < 0:
            line[1] += length
        # When length is 0
        if line[1] == 0:
            line[1] = length
        # print(line[0], line[1])
        print(string[line[0]:line[1]])