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

lines = []
for a in range(0, 4):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a]) - 1):
        lines[a][b] = int(lines[a][b])
    if ord('1') <= ord(lines[a][2]) <= ord('9'):
        lines[a][2] = int(lines[a][2])
    else:
        lines[a][2] = ord(lines[a][2]) - 55

totalPay = []
for run in range(0, len(lines)):
    line = lines[run]
    location, start, end = line[0], line[1], line[2]
    times = [start, end]
    # Change numbers to times
    for change in range(0, len(times)):
        time, cTime = times[change] - 1, 9
        cTime += time * 0.5
        times[change] = cTime
    #print(location, times[0], times[1])
    workTime = times[1] - times[0]
    #print(workTime)
    if 1 <= location <= 9:
        payment = 10
        paid1 = workTime * payment
        totalPay.append(paid1)
        print('$' + str(paid1) + '0')
    elif 10 <= location <= 19:
        payment = 8
        if workTime <= 4:
            paid2 = payment * workTime
            totalPay.append(paid2)
            print('$' + str(paid2) + '0')
        elif workTime > 4:
            paid2 = payment * 4
            workTime -= 4
            payment = 12
            paid2 += workTime * payment
            totalPay.append(paid2)
            print('$' + str(paid2) + '0')
    elif 20 <= location <= 29:
        payment = 12
        if workTime <= 4:
            paid3 = payment * workTime
            totalPay.append(paid3)
            print('$' + str(paid3) + '0')
        elif workTime > 4:
            paid3 = payment * 4
            workTime -= 4
            payment = 24
            paid3 += workTime * payment
            totalPay.append(paid3)
            print('$' + str(paid3) + '0')

totalPaid = 0
for add in range(0, len(totalPay)):
    totalPaid += totalPay[add]
print('$' + str(totalPaid) + '0')