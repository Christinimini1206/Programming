"""
18, 44, 7, 21, 23
18, 44, 31, 22, 38
18, 44, 31, 34, 21
18, 44, 31, 5, 9

2, 18, 33, 49, 41
9, 22, 29, 45, 48
1, 17, 34, 50, 25
4, 17, 20, 33, 46
11, 24, 37, 34, 50
"""

# Input
lines = []
for a in range(0, 4):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

# Run each line
for run in range(0, len(lines)):
    line = lines[run]
    # Identify each card
    checkedCards = []
    for check in range(0, len(line)):
        # Diamonds (1-13)
        if 1 <= line[check] <= 13:
            checkedCards.append(['D', line[check]])
        # Hearts (14-26)
        elif 14 <= line[check] <= 26:
            checkedCards.append(['H', line[check] - 13])
        # Spades (27-39)
        elif 27 <= line[check] <= 39:
            checkedCards.append(['S', line[check] - 26])
        # Clubs (40-52)
        elif 40 <= line[check] <= 52:
            checkedCards.append(['C', line[check] - 39])
    checkedCards.sort()
    # Identify the hand
    pair = [[checkedCards[0][1]], []]
    for p in range(1, len(checkedCards)):
        num = checkedCards[p][1]
        if num in pair[0]:
            pair[0].append(num)
        else:
            pair[1].append(num)
    sames = [0, 0]
    for lst in range(0, len(pair)):
        # Check if all the numbers in the list are the same
        number = pair[lst][0]
        for sameN in range(0, len(pair[lst])):
            if pair[lst][sameN] == number:
                sames[lst] += 1
    if sames[0] == 2:
        print('PAIR')
    elif sames[0] == 3 and sames[1] == 2:
        print('FULL HOUSE')
    elif sames[0] == 3 and sames[1] != 2:
        print('THREE OF A KIND')
    elif sames[0] != 2 and sames[1] == 3:
        print('THREE OF A KIND')
    elif sames[0] == 4:
        print('FOUR OF A KIND')
    else:
        print('NONE')