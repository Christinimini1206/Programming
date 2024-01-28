"""
1 5
1 2

2 5
1 2
5 10

2 5
1 10
5 10
"""

N, T = map(int, input().split())
days = [list(map(int, input().split())) for i in range(N)]
daysFull = []
indexD, reachedLimit = 0, False

# Fill in the days without any additional food provided
for i in range(T):
    if indexD < len(days) and days[indexD][0] == i + 1:
        daysFull.append(days[indexD])
        indexD += 1
    else:
        daysFull.append([i + 1, 0])

bessieEats = [0] * T
inStock = days[0][1]
for d in range(T):
    if d != 0 and daysFull[d][0] == d + 1:
        inStock += daysFull[d][1]
    if inStock != 0:
        inStock -= 1
        bessieEats[d] += 1
    print(inStock, bessieEats)
print(bessieEats.count(1))
