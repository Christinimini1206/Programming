"""
5 6
4 1
4 2
4 3
2 5
1 2
1 5
"""


def checkTheNumber(number):
    for letter in str(number):
        if int(letter) not in range(1, 5):
            return False
    return True


def compareTheNumber(number, pair):
    # print(number)
    number = list(str(number))
    for p in pair:
        ind1, ind2 = p[0] - 1, p[1] - 1
        # print(number[ind1], number[ind2])
        if number[ind1] == number[ind2]:
            return False
    return True


'''Input'''
fin = open("revegetate.in", 'r')
fout = open('revegetate.out', 'w')

N, M = map(int, fin.readline().strip().split())
pairs = [list(map(int, fin.readline().strip().split())) for i in range(M)]
'''
theNum = 0
for n in range(int('1' * N), int('4' * N) + 1):
    if not checkTheNumber(n):
        continue
    else:
        if not compareTheNumber(n, pairs):
            continue
        else:
            theNum = n
            break
        # print(compareTheNumber(n, pairs))
    # print('')
'''
tag = True
place = [1] * N
# pairs.sort()
counter = 0
while tag:
    tag = False
    for x, y in pairs:
        counter += 1
        if place[x - 1] == place[y - 1]:
            place[max(x, y) - 1] += 1
            print(place)
            tag = True
            break
print(counter)

fout.write(f"{''.join(map(str, place))}\n")
fout.close()

# 112312222
# 112314222





