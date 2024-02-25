"""
8, 7, 2, 0
0

1, 3, 6, 8, 0
1, 3, 5, 7, 9, 0
2, 4, 5, 6, 0
2, 4, 6, 8, 10, 0
4, 0
"""

l1 = input().split(', ')
l2 = input().split(', ')
l3 = input().split(', ')
l4 = input().split(', ')
l5 = input().split(', ')
lines = [l1, l2, l3, l4, l5]

for a in range(0, len(lines)):
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for a in range(0, len(lines)):
    line = lines[a]
    if line[0] == 0:
        print('1/1')
    else:
        even, odd = 1, 1
        for b in range(0, len(line)):
            if line[b] == 1:
                odd += 16
            elif line[b] == 2:
                even += 16
            elif line[b] == 3:
                odd += 8
            elif line[b] == 4:
                even += 8
            elif line[b] == 5:
                odd += 4
            elif line[b] == 6:
                even += 4
            elif line[b] == 7:
                odd += 2
            elif line[b] == 8:
                even += 2
            elif line[b] == 9:
                odd += 1
            elif line[b] == 10:
                even += 1
        string = ''
        string += str(even)
        string += '/'
        string += str(odd)
        print(string)