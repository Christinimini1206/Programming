from itertools import combinations
import itertools

"""
ID: ldoyun81
LANG: PYTHON3
TASK: wormhole
"""

"""
def isInfLoop(chain):
    '''
    start
    pairout
    next
    '''
    return 'asdf'


def get_teams(list_of_ppl, size=2):
    if len(list_of_ppl) > size:
        for team in combinations(list_of_ppl, size):
            for teams in get_teams(list(set(list_of_ppl) - set(team))):
                yield [list(team), *teams]
    else:
        yield [list_of_ppl]


'''Input'''
fin = open("wormhole.in", 'r')
fout = open('wormhole.out', 'w')

inp = fin.read().strip().split('\n')
wormN = int(inp[0])
loc = [tuple(map(int, i.split(' '))) for i in inp[1:]]
print(loc)

total = []
for team in get_teams(loc):
    total.append(team)
print(total)





print(total)
'''Find all the possible cases of pairs'''
possible = list(itertools.permutations(loc))
minAx, maxAx = 0, 0
for s in possible:
    for pt in s:
        if min(pt) < minAx:
            minAx = min(pt)
        if max(pt) > maxAx:
            maxAx = max(pt)

char = -1
for ch in range(len(possible)):
    emptyGrid = [[''] * (maxAx - minAx + 1)] * (maxAx - minAx + 1)
    if ch % 2 == 0:
        for pt in range(0, len(possible[ch])):
            if pt % 2 == 0:
                char += 1
                emptyGrid[possible[ch][pt][0]][possible[ch][pt][1]] = chr(ord('a') + char) + '1'
            else:
                emptyGrid[possible[ch][pt][0]][possible[ch][pt][1]] = chr(ord('a') + char) + '2'

print(emptyGrid)

'''
# Remove all the duplicates
posOrganized = []
existing = False
for s in possible:
    lst = []
    for ele in range(0, len(s)):
        if ele % 2 == 0:
            lst.append([])
        lst[-1].append(s[ele])
    posOrganized.append(lst)
    existing = False
    for el in range(len(posOrganized)):
        equal = 0
        for i in range(len(lst)):
            print(sorted(lst[i]), sorted(posOrganized[el][i]))
            if sorted(lst[i]) == sorted(posOrganized[el][i]):
                equal += 1

        if equal == len(lst):
            existing = True
            break
        print('')
    if existing == False:
        posOrganized.append(lst)
'''
'''
grid = sorted(loc, key=lambda x: (x[1], x[0]))


for lst in possible:
    count = 0
    if isInfLoop(lst):
        count += 1
print(count)
'''
'''Test each case of pairs'''
'''
d = list(itertools.product(*possible))
for x in d:
    print(x)
'''

'''Output'''
fout.write(f'{2}\n')
fout.close()"""

def initialize(iteration_n):
    p = sorted(iteration_n, key = lambda x: (x[1],x[0]))
    sectioned_points, ends = divide_points(p)
    return sectioned_points, ends

def initialize1(fin):
    N = int(fin.readline().strip())
    wormhole = []

    for i in range(N):
        x, y = map(int, fin.readline().strip().split())
        wormhole.append((x,y))

    def recur_foo(wormhole):
        if len(wormhole) > 2:
            for pair in ([wormhole[0], i] for i in wormhole[1:]):
                for holes in recur_foo(list(set(wormhole) - set(pair))):
                        yield [pair, *holes]
        else:
            yield [wormhole]

    possible_pairs_of_wormhole = [sum(i, []) for i in list(recur_foo(wormhole))]
#    print(possible_pairs_of_wormhole)
    return possible_pairs_of_wormhole#[:len(possible_pairs_of_wormhole)//2]

def divide_points(sorted_list):
    result = []
    temp = []
    ends = []
    for ind in range(len(sorted_list)):
        temp.append(sorted_list[ind])
        try:
            if sorted_list[ind][1] != sorted_list[ind +1][1]:
                result.append(temp)
                ends.append(sorted_list[ind])
                temp = []
        except IndexError:
            result.append(temp)
            ends.append(sorted_list[ind])
    return result, ends

def find_next_one(pair, sectioned_points, ends):
    for ind, value in enumerate(sectioned_points):
        try:
            temp = value.index(pair)
            return sectioned_points[ind][temp +1]

        except ValueError:
            continue

def is_inf_loop(iteration_n, sectioned_points, ends):
    idx_list = []
    curr = 0
    for curr, value in enumerate(iteration_n):
        if (curr in idx_list):
            continue
        else:
            loop_list = []
            while True:
                loop_list.append(curr)
                if curr % 2 == 0:
                    curr = curr + 1
                else:
                    curr = curr -1
                                            # 1st, pair, next
                pair = iteration_n[curr]
                if pair not in ends:
                    next_one = find_next_one(pair, sectioned_points, ends)
                else:
                    idx_list += loop_list
                    break
                curr = iteration_n.index(next_one)
                if curr in loop_list:
                    return True
    return False

def solve():
    fin = open('wormhole.in','r')
    fout = open('wormhole.out','w')
    possible_wormhole = initialize1(fin)
    sectioned_points, ends = initialize(possible_wormhole[0])

    count = 0
#    ans = []
    for i in possible_wormhole:
        if is_inf_loop(i, sectioned_points, ends):
#            ans.append(i)
            count += 1
    fout.write('{0:}\n'.format(count))
    fout.close()
#    return ans
solve()