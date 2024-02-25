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

lines = []
for a in range(0, 4):
    lines.append(input().split(', '))
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for run in range(0, len(lines)):
    line = lines[run]
    par, score = line[0], line[1]
    result = score - par
    if result == -1:  # Birdie
        print('birdie')
    elif result == -2:  # Eagle
        print('eagle')
    elif result == 1:  # Bogey
        print('bogey')
    elif result == 2:  # Double bogey
        print('double bogey')
    elif result == 0:
        print('par')

# Cumulative Score
parC, scoreC = 0, 0
for add in range(0, len(lines)):
    parC += lines[add][0]
    scoreC += lines[add][1]
resultC = scoreC - parC
if resultC == -1:
    print('1 below par')
elif resultC == -2:
    print('2 below par')
elif resultC == 1:
    print('1 over par')
elif resultC == 2:
    print('2 over par')
elif resultC == 0:
    print('par')

