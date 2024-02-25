"""
5, 9, H
11, 1, 7
19, 3, F
25, 2, B

3, 9, H
17, 1, E
20, 5, G
15, 2, 8
"""

# Input
lines = [input().split(', '),
         input().split(', '),
         input().split(', '),
         input().split(', ')]
allMoney = 0

# Change numbers to integer
for a in range(0, len(lines)):
    totalMoney = 0
    for b in range(0, len(lines[a]) - 1):
        lines[a][b] = int(lines[a][b])
    if ord('1') <= ord(lines[a][-1]) <= ord('9'):
        lines[a][-1] = int(lines[a][-1])

    start, end = lines[a][1], lines[a][2]

    times = [start, end]
    # Convert times
    for b in range(0, len(times)):
        if times[b] == 1:
            times[b] = 9.0
        elif times[b] == 2:
            times[b] = 9.5
        elif times[b] == 3:
            times[b] = 10.0
        elif times[b] == 4:
            times[b] = 10.5
        elif times[b] == 5:
            times[b] = 11.0
        elif times[b] == 6:
            times[b] = 11.5
        elif times[b] == 7:
            times[b] = 12.0
        elif times[b] == 8:
            times[b] = 12.5
        elif times[b] == 9:
            times[b] = 13.0
        elif times[b] == 'A':
            times[b] = 13.5
        elif times[b] == 'B':
            times[b] = 14.0
        elif times[b] == 'C':
            times[b] = 14.5
        elif times[b] == 'D':
            times[b] = 15.0
        elif times[b] == 'E':
            times[b] = 15.5
        elif times[b] == 'F':
            times[b] = 16.0
        elif times[b] == 'G':
            times[b] = 16.5
        elif times[b] == 'H':
            times[b] = 17.0
    start, end = times[0], times[1]
    totalTime = times[1] - times[0]
    # print(start, end, totalTime)

    location = lines[a][0]
    # Check for location
    if 1 <= location <= 9:
        totalTime *= 10.00
        totalMoney += totalTime
    elif 10 <= location <= 19:
        if totalTime <= 4:
            totalTime *= 8.00
            totalMoney += totalTime
        elif totalTime > 4:
            first4 = 4 * 8.00
            totalTime -= 4
            totalTime *= 12.00
            totalMoney += first4
            totalMoney += totalTime
    elif 20 <= location <= 29:
        if totalTime <= 4:
            totalTime *= 12.00
            totalMoney += totalTime
        elif totalTime > 4:
            first4 = 4 * 12.00
            totalTime -= 4
            totalTime *= 24.00
            totalMoney += first4
            totalMoney += totalTime
    allMoney += totalMoney
    totalMoneyStr = '$' + str(totalMoney) + '0'
    print(totalMoneyStr)
print('$' + str(allMoney) + '0')