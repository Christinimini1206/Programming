"""
4
24
16
10
20

25
100
55
36
1
"""

lines = []
for a in range(0, 5):
    lines.append(int(input()))
for run in range(0, len(lines)):
    line = lines[run]
    squares, colored = 0, 0  # Number of squares & colored squares
    addS, addC = 4, 2
    coloredSquares = 0  # Total colored squares
    area = 0  # Total area of colored squares
    while line >= 1:
        # Get the number of squares
        squares = addS
        line /= 2  # Get the divided side length
        addS = squares * 2 + 2

        # Get the number of colored squares
        colored = addC
        addC = colored * 2 + 2

        coloredSquares = squares - colored  # Not colored squares
        area += (line ** 2) * coloredSquares  # Area of total colored squares
    if '.0' == str(area)[len(str(area)) - 2:]:
        area = int(area)
    print(area)
