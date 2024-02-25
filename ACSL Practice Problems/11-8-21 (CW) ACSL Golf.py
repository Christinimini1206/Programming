"""
5, 4
3, 5
4, 5
3, 2

4, 2
5, 6
3, 3
3, 4
"""

l1 = input().split(', ')
l2 = input().split(', ')
l3 = input().split(', ')
l4 = input().split(', ')
lines = [l1, l2, l3, l4]

for a in range(0, len(lines)):
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

cumulative = 0
for a in range(0, len(lines)):
    cumulative += lines[a][1]
total = cumulative

for a in range(0, len(lines)):
    line = lines[a]
    par, score = line[0], line[1]
    par -= score
    if par == -1:
        print('bogey')
        cumulative += 1
    elif par == -2:
        print('double bogey')
        cumulative += 2
    elif par == 1:
        print('birdie')
        cumulative -= 1
    elif par == 2:
        print('eagle')
        cumulative -= 2
    else:
        print('par')

differ = abs(cumulative - total)
if cumulative > total:
    print(differ, 'over par')
elif cumulative < total:
    print(differ, 'under par')
else:
    print('par')
