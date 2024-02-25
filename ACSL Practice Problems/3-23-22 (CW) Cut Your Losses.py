"""
4 5 -9 2 0
"""

line = input().split(' ')
for a in range(0, len(line)):
    line[a] = int(line[a])

value = 0
for b in range(0, len(line)):
    if line[b] > 0:
        value += line[b]

print(value)