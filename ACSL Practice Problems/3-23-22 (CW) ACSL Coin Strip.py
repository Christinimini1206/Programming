"""
12, 7, 1, 4, 6, 8, 9, 10, 12
14, 6, 1, 3, 6, 7, 10, 14
10, 2, 4, 9
10, 2, 6, 10

6, 3, 3, 5, 6
8, 2, 4, 7
15, 5, 1, 7, 8, 14, 15
15, 6, 2, 4, 6, 8, 10, 15
7, 3, 4, 6, 7
"""

lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for run in range(0, len(lines)):
    line = lines[run]
    stripLen, numCoin, coins = line[0], line[1], line[2:]
    strip = []
    # Create a coin strip
    for coin in range(0, stripLen):
        strip.append(0)
    # Put coins on their places
    for coin2 in range(0, len(coins)):
        strip[coins[coin2] - 1] = 1
    strip.reverse()
    # Check if coins could move to the left
    movement = 1
    totalMove = []
    coins.reverse()
    for squares in range(0, 5):
        canMove = 0
        for move in range(0, len(coins)):
            coinLoc = stripLen + 1 - coins[move]
            nextLoc = strip[coinLoc:coinLoc + movement]
            if 1 not in nextLoc and len(nextLoc) == movement:
                canMove += 1
        totalMove.append(canMove)
        movement += 1
    # Output
    finalStr = ''
    for fin in range(0, len(totalMove) - 1):
        finalStr += str(totalMove[fin])
        finalStr += ', '
    finalStr += str(totalMove[-1])
    print(finalStr)

