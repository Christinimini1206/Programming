"""
3, 1, A, 3, C, 8, A
3, 1, A, 6, C, 8, B
3, 1, B, 6, B, 9, C
2, 1, C, 5, B
2, 3, B, 7, A

4, 1, A, 2, B, 8, A. 9, B
3, 1, A, 2, B, 9, A
3, 3, C, 6, B, 7, C
2, 7, A, 6, C
2, 1, C, 6, A
"""

lines = []
# Input
for a in range(0, 1):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        if ord('1') <= ord(lines[a][b]) <= ord('9'):
            lines[a][b] = int(lines[a][b])

for run in range(0, len(lines)):
    line = lines[run]
    pts, NofPts = [], line[0]
    grid = ['1', '2', '3',
            '4', '5', '6',
            '7', '8', '9']

    # Divide into separate points
    for dPts in range(1, len(line) - 1):
        if dPts % 2 != 0:
            pts.append([])
            pts[-1].append(line[dPts])
            pts[-1].append(line[dPts + 1])
    print(pts)

    # Replace 'number' with letters with points
    '''for rPts in range(0, len(pts)):
        point = pts[rPts]
        grid[point[0] - 1] = point[1]'''

    # Possible combination
    posComb = [['A', 'B', 'C'],
               ['A', 'C', 'B'],
               ['B', 'A', 'C'],
               ['B', 'C', 'A'],
               ['C', 'A', 'B'],
               ['C', 'B', 'A']]
