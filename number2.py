N = int(input())
infected = input()

counting = 0
ones = []
for i in infected:
    if i == "1":
        counting += 1
    else:
        if counting != 0:
            ones.append(counting)
            counting = 0
if counting != 0:
    ones.append(counting)


def calculateMax(infected, N, ones):
    if infected == "1" * N:
        return 1
    if len(infected) == 0 or infected == "0" * N:
        return 0
    if infected[0] == "1":
        left = True
    else:
        left = False

    if infected[-1] == "1":
        right = True
    else:
        right = False

    nightsPassed = ones[0]
    if left == right == True:
        for i in range(1, len(ones) - 1):
            temp = ones[i] // 2 - (1 if ones[i] % 2 == 0 else 0)
            nightsPassed = min(nightsPassed, temp)
        nightsPassed = min(nightsPassed, ones[0] - 1)
        nightsPassed = min(nightsPassed, ones[-1] - 1)
    elif left == True and right == False:
        for i in range(1, len(ones)):
            temp = ones[i] // 2 - (1 if ones[i] % 2 == 0 else 0)
            nightsPassed = min(nightsPassed, temp)
        nightsPassed = min(nightsPassed, ones[0] - 1)
    elif left == False and right == True:
        for i in range(0, len(ones) - 1):
            temp = ones[i] // 2 - (1 if ones[i] % 2 == 0 else 0)
            nightsPassed = min(nightsPassed, temp)
        nightsPassed = min(nightsPassed, ones[-1] - 1)
    elif left == right == False:
        for i in range(0, len(ones)):
            temp = ones[i] // 2 - (1 if ones[i] % 2 == 0 else 0)
            nightsPassed = min(nightsPassed, temp)

    answer = 0
    if left == right == True:
        for i in range(1, len(ones) - 1):
            answer += ones[i] - 2 * nightsPassed
        if ones[0] - 2 * nightsPassed <= 0:
            answer += 1
        else:
            answer += ones[0] - 2 * nightsPassed

        if ones[-1] - 2 * nightsPassed <= 0:
            answer += 1
        else:
            answer += ones[-1] - 2 * nightsPassed
    elif left == True and right == False:
        for i in range(1, len(ones)):
            answer += ones[i] - 2 * nightsPassed
        if ones[0] - 2 * nightsPassed <= 0:
            answer += 1
        else:
            answer += ones[0] - 2 * nightsPassed
    elif left == False and right == True:
        for i in range(0, len(ones) - 1):
            answer += ones[i] - 2 * nightsPassed
        if ones[-1] - 2 * nightsPassed <= 0:
            answer += 1
        else:
            answer += ones[-1] - 2 * nightsPassed
    elif left == right == False:
        for i in range(0, len(ones)):
            answer += ones[i] - 2 * nightsPassed
    return answer


print(calculateMax(infected, N, ones))