import datetime
now = datetime.datetime.now()

"""
2 4
7 9

2 3
1 10

5 4
7 9 13 17 21
"""

N, K = map(int, input().split())  # Days and fixed cost
days = list(map(int, input().split()))  # Days watching
cost = lambda x: x + K

# continuous = cost(end - start + 1)
# descrete = 2 * cost(1)

minimum = None

for ind, val in enumerate(days):
    for ind2 in range(ind + 1, len(days)):
        temp = cost(days[ind2] - days[ind] + 1) + (len(days) - ind2 + ind - 1) * cost(1)
        if minimum is None:
            minimum = temp
        elif minimum > temp:
            minimum = temp

print(minimum)

end = datetime.datetime.now()
print("Total run time:", end - now)

'''
for i in range(N - 1):
    for ii in range(i + 1, N):
        print(i, ii)
        break
'''