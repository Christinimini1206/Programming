"""
4 5 3
1 3 4 6 9
2 4 5 7 8
1 2 6 9 10
1 2 3 4 7
2
4
1
"""

N, K, Q = input().split(' ')
N, K, Q = int(N), int(K), int(Q)

runs = []
for i in range(N):
    runs.append(input().split(' '))
    runs[-1] = list(map(int, runs[-1]))

s = [int(input()) for a in range(Q)]

# Groups columns as rows
column = [[]] * K
for col in range(0, K):
    column[col] = [runs[a][col] for a in range(len(runs))]

for ch in s:
    large, small = max(column[ch - 1]), min(column[ch - 1])
    print(large - small)