"""
1, 8, 2, R
2, 8, 2, N, R, B
2, 8, 2, Y, R, B

1, 7, 7, B
2, 4, 8, Y, B, R
2, 5, 11, Y, R, R
2, 6, 8, N, B, R
2, 10, 8, N, B, B
"""

lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    for b in range(0, 3):
        lines[a][b] = int(lines[a][b])

for runT in range(0, len(lines)):
    line = lines[runT]
    numOfM = line[0]
    red, blue= line[1], line[2]
    sumRB = red + blue
    # Case 1
    if numOfM == 1:
        selected = line[-1]
        if selected == 'R':
            print(str(red) + '/' + str(sumRB))
        else:
            print(str(blue) + '/' + str(sumRB))
    # Case 2 or 3
    else:
        replace = line[3]
        orders = [line[4], line[5]]
        numer = 1
        # Case 2
        if replace == 'Y':
            for color in range(0, len(orders)):
                if orders[color] == 'R':
                    numer *= red
                else:
                    numer *= blue
            print(str(numer) + '/' + str(sumRB ** 2))
        # Case 3
        else:
            for color in range(0, len(orders)):
                if orders[color] == 'R':
                    numer *= red
                    red -= 1
                else:
                    numer *= blue
                    blue -= 1
            print(str(numer) + '/' + str((sumRB - 1) * sumRB))
