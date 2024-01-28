"""
ID: ldoyun81
LANG: PYTHON3
TASK: ride
"""

# Inputs
'''
COMETQ
HVNGAT

ABSTAR
USACO
'''

comet, group = input(), input()
lstC, lstG = [], []
lst1 = [comet, group]
lst2 = [lstC, lstG]
for a in range(0, 2):
    for b in range(0, len(lst1[a])):
        lst2[a].append(ord(lst1[a][b]) - 64)

numC, numG = 1, 1
numbers = [numC, numG]
for a in range(0, 2):
    for b in range(0, len(lst2[a])):
        numbers[a] *= lst2[a][b]

place = ''
if numbers[0] % 47 == numbers[1] % 47:
    place = 'GO'
    print(place)
else:
    place = 'STAY'
    print(place)
