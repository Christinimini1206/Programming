"""
2, 8, H
3, 10, S
4, 11, D
3, 10, N
5, 13, C

2, 10, H
1, 7, S
2, 9, D
1, 8, N
5, 12, N
"""

# Input
lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a]) - 1):
        lines[a][b] = int(lines[a][b])

# Run the code
for run in range(0, len(lines)):
    line = lines[run]
    bid, trick, card = line[0], line[1], line[2]
    linePt = bid + 6  # Line of the point
    bidAbove = trick - linePt  # Calculating for points above the line
    ptUnder, ptAbove = 0, 0  # Under & above
    # Add the points according to the cards
    if card == 'H' or card == 'S':
        ptUnder = bid * 30
        ptAbove = bidAbove * 30
    elif card == 'C' or card == 'D':
        ptUnder = bid * 20
        ptAbove = bidAbove * 20
    elif card == 'N':
        other = 0
        for above in range(0, bid):
            ptUnder += 40 - other
            other = 10
        ptAbove = bidAbove * 30
    print(str(ptUnder) + ', ' + str(ptAbove))


