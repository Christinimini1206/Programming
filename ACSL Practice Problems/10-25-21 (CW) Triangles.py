"""
2, 3, 4, 4, 3, 2
3, 4, 5, 5, 2, 3
2, 3, 4, 2, 3, 4.5
2, 2, 3, 3.5, 2, 2
2, 2, 2, 1, 2, 2.5

3, 4, 5, 3, 4, 5
5, 7, 11, 11, 7, 6
6, 8, 10, 4, 6, 8
6, 8, 10, 5, 7, 12
9, 12, 15, 12, 9, 15
"""

l1 = input().split(', ')
l2 = input().split(', ')
l3 = input().split(', ')
l4 = input().split(', ')
l5 = input().split(', ')
lines = [l1, l2, l3, l4, l5]

for a in range(0, len(lines)):
    for b in range(0, len(lines[a])):
        lines[a][b] = float(lines[a][b])

for a in range(0, len(lines)):
    line = lines[a]
    t1, t2 = line[0:3], line[3:6]
    t1.sort()
    t2.sort()
    # print(t1, t2)
    pair = 0
    for b in range(0, 3):
        for c in range(0, 3):
            if t1[b] == t2[c]:
                pair += 1
                t1[b], t2[c] = 100, 100
        # print(t1, t2)
    print(pair)