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

    left, right = None, None
    if infected[0] == "1":
        left = ones.pop(0)
    if infected[-1] == "1":
        right = ones.pop(-1)

    num = min(ones)
    if num % 2 == 0:
        nightsPassed = num // 2 - 1
    else:
        nightsPassed = num // 2

    if left != None:
        nightsPassed = min(nightsPassed, left - 1)
    if right != None:
        nightsPassed = min(nightsPassed, right - 1)

    answer = 0
    for i in range(len(ones)):
        answer += ones[i] - 2 * nightsPassed
    if left != None:
        if left - 2 * nightsPassed <= 0:
            answer += 1
        else:
            answer += left - 2 * nightsPassed
    if right != None:
        if right - 2 * nightsPassed <= 0:
            answer += 1
        else:
            answer += right - 2 * nightsPassed
    return answer


print(calculateMax(infected, N, ones))