"""
3, 3, 2
4, 1, 1
5, 3, 2
5, 4, 3
2, 3, 1

1, 1, 4
2, 4, 1
4, 2, 3
1, 3, 2
3, 2, 2
"""

l1 = input().split(', ')
l2 = input().split(', ')
l3 = input().split(', ')
l4 = input().split(', ')
l5 = input().split(', ')
lines = [l1, l2, l3, l4, l5]

for a in range(0, len(lines)):
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for a in range(0, len(lines)):
    grid = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5],
            [4, 1], [4, 2], [4, 3], [4, 4], [4, 5],
            [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
            [2, 1], [2, 2], [2, 3], [2, 4], [2, 5],
            [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
    queen = lines[a]

    # Ordered pair & the cells that the queen can move
    location, N = [queen[0], queen[1]], queen[2]
    qLocate = grid.index(location)
    grid[qLocate] = ' Q  '
    '''
    if 0 <= qLocate <= 4:
    elif 5 <= qLocate <= 9:
    elif 10 <= qLocate <= 14:
    elif 15 <= qLocate <= 19:
    elif 20 <= qLocate <= 24:
    '''
    # Grid divided as rows
    row1, row2, row3, row4, row5 = grid[0:5], grid[5:10], grid[10:15], grid[15:20], grid[20:25]
    gridR = [row1, row2, row3, row4, row5]

    # Find rows
    row = []
    for b in range(0, len(grid)):
        if grid[b][0] == location[0]:
            row.append(grid[b])
    front, back = row[0], row[-1]
    frontN, backN = grid.index(front), grid.index(back)
    print(frontN, backN, grid.index(' Q  '))

    # Find columns
    # Find diagonals

    print(location)
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print('')