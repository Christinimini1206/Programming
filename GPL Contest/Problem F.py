import time

n = int(input())
loc = list(map(int, input().split(' ')))

timeBTotal, timeUTotal = [], []
for ch in range(len(loc)):
    obj = loc[ch]
    timeBTotal.append([])

    for on in range(1, n + 1):
        # Go below
        timeB = 0
        while obj != on:
            print(obj, on)

            obj -= 1
            timeB += 1
            if obj < 1:
                obj = on
            if obj == on:
                break
        timeBTotal[-1].append(timeB)
        # print(timeBTotal)
        """# Go up
        timeUTotal.append([])
        timeU = 0
        obj = loc[ch]
        while obj != on:
            obj += 1
            timeU += 1
            if obj > on:
                obj = 1
            if obj == on:
                break
            print(obj, on)
            time.sleep(0.2)

        timeUTotal[-1].append(timeU)
        print(timeUTotal)"""

print(timeBTotal)
# print(timeUTotal)