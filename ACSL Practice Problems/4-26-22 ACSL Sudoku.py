"""
0,5,0,0,1,0,0,4,0
1,0,7,0,0,0,6,0,2
0,0,0,9,0,5,0,0,0
2,0,8,0,3,0,5,0,1
0,4,0,0,7,0,0,2,0
9,0,1,0,8,0,4,0,6
0,0,0,4,0,1,0,0,0
3,0,4,0,0,0,7,0,9
0,2,0,0,6,0,0,1,0
4,2
4,8
6,8
8,8
3,5

0,0,2,0,0,0,5,0,0
0,1,0,7,0,5,0,2,0
4,0,0,0,9,0,0,0,7
0,4,9,0,0,0,7,3,0
8,0,1,0,3,0,4,0,9
0,3,6,0,0,0,2,1,0
2,0,0,0,8,0,0,0,4
0,8,0,9,0,2,0,6,0
0,0,7,0,0,0,8,0,0
2,3
7,7
4,4
5,8
3,6
"""

# Input
grid, rowCol = [], []
for a in range(0, 14):
    if a < 9:  # Grid
        grid.append(input().split(','))
        for b in range(0, len(grid[a])):
            grid[a][b] = int(grid[a][b])
    elif a >= 9:  # Rows and columns
        rowCol.append(input().split(','))
        for b in range(0, 2):
            rowCol[-1][b] = int(rowCol[-1][b])

# Run the code
for run in range(0, len(rowCol)):
    pt = rowCol[run]
    row, col = pt[0], pt[1]
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    posNum = []
    # Check the row
    for cR in range(0, len(nums)):
        if nums[cR] not in grid[row - 1]:
            posNum.append(nums[cR])
    # Check the column
    column = []
    for c in range(0, len(grid)):  # Make the column
        column.append(grid[c][col - 1])
    posNum2 = []
    for cC in range(0, len(posNum)):
        if posNum[cC] not in column:
            posNum2.append(posNum[cC])
    # Check the squares
    rows, cols = 0, 0
    if 1 <= row <= 3:
        rows = 0
        if 1 <= col <= 3:  # Square 1
            cols = 0
        elif 4 <= col <= 6:  # Square 4
            cols = 3
        elif 7 <= col <= 9:  # Square 7
            cols = 7
    elif 4 <= row <= 6:
        rows = 3
        if 1 <= col <= 3:  # Square 2
            cols = 0
        elif 4 <= col <= 6:  # Square 5
            cols = 3
        elif 7 <= col <= 9:  # Square 8
            cols = 6
    elif 7 <= row <= 9:
        rows = 6
        if 1 <= col <= 3:  # Square 3
            cols = 0
        elif 4 <= col <= 6:  # Square 6
            cols = 3
        elif 7 <= col <= 9:  # Square 9
            cols = 6
    square = []
    # Check the squares
    for sqr in range(rows, rows + 3):  # Create the square
        for sqrC in range(cols, cols + 3):
            square.append(grid[sqr][sqrC])
    posNum3 = []
    for cS in range(0, len(posNum2)):
        if posNum2[cS] not in square:
            posNum3.append(posNum2[cS])
    # Final string
    fString = ''
    for fStr in range(0, len(posNum3) - 1):
        fString += str(posNum3[fStr])
        fString += ','
    fString += str(posNum3[-1])
    print(fString)
