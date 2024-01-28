"""
3
1 2 1
3 2 1
1 3 1
"""

N = int(input())
lines = [list(map(int, input().split())) for l in range(N)]
for l in range(N):
    for ll in range(len(lines[l])):
        lines[l][ll] -= 1

# Test all the cases where the pebble starts in different location
maxPoint = 0
for case in range(3):
    points = 0
    array = [0] * 3
    array[case] += 1

    # Swapping process
    for p in range(len(lines)):
        switch = lines[p][0:2]
        # Swap a and b
        a = array[switch[0]]
        b = array[switch[1]]
        array[switch[1]] = a
        array[switch[0]] = b

        # Check for the point
        checking = lines[p][2]
        if array[checking] == 1:
            points += 1
    if points > maxPoint:
        maxPoint = points
print(maxPoint)
