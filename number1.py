# Input
N, M = map(int, input().split())
cows = list(map(int, input().split()))
candy = list(map(int, input().split()))

# Run for candies
for c in candy:
    base = 0
    # If the first candy is eaten by the first cow
    if c <= cows[0]:
        cows[0] += c
        continue
    else:
        for cow in range(len(cows)):
            if c >= cows[cow] >= base:
                temp = cows[cow]
                cows[cow] += cows[cow] - base
                base = temp
            elif cows[cow] >= c:
                cows[cow] += c - base
                break

for fin in cows:
    print(fin)