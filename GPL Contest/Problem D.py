import time

start = time.time()

N, X = map(int, input().split())

# bits = [int(input()) for i in range(N) if ]
bits = []
count = []
for i in range(N):
    inputN = int(input())
    if inputN > X:
        continue
    elif inputN > X / 2:
        count.append(inputN)
    else:
        bits.append(inputN)
bits.sort()


total = 0
ans = 0
for i in bits:
    if total < X / 2:
        total += 1
        ans += 1
    break

if min(count) < (X - total):
    ans += 1

"""

total = []
for num in bits:
    total.append(num)
    if sum(total) > X:
        total.pop()
        break
print(len(total))
"""

end = time.time()
print(end - start)