"""
ID: ldoyun81
LANG: PYTHON3
TASK: barn1
"""

'''
3  1
4  2
6  2
8  6
14  1
15  1
16  1
17  4
21  4
25  1
26  1
27  3
30  1
31  9
40  1
41  1
42  1
43 
'''

'''INPUT'''
fin = open("barn1.in", 'r')
fout = open('barn1.out', 'w')

inp = fin.read().strip().split('\n')

'''
- Only get the list containing adjacent occupied stalls
    - ex.) ['cc', 'ccc']
    - Get the index number of the stalls as well
- Try each possible combination of the adjacent stalls and check which one covers
the least number of stalls
'''

M, S, C = map(int, inp[0].split(' '))

occupied = inp[1:]
occupied = [int(occupied[i]) for i in range(0, len(occupied))]
occupied.sort()

'''GET THE DIFFERENCES'''
diff = []
for d in range(0, len(occupied) - 1):
    diff.append(occupied[d + 1] - occupied[d])

'''FIND THE LARGEST GAP'''
counting = 0
for div in range(0, M - 1):
    try:
        largeLoc = diff.index(max(diff))
        diff.pop(largeLoc)
        counting += 1
    except:
        IndexError
        break
# find_gaps = [rooms[ind + 1] - num for ind, num in enumerate(rooms[:-1])]
'''
lst, part = [], [occupied[0]]
for grp in range(1, len(occupied)):
    if occupied[grp] - occupied[grp - 1] == 1:
        part.append(occupied[grp])
    else:
        lst.append(part)
        part = [occupied[grp]]
lst.append(part)

print(lst)

print('{0:0=4}'.format(123))
for div in range(10 ** (M - 1), 10 ** (M - 1) * (len(lst) - 1) + 1):
    grouped = []
    num = list(str(div))
    num.sort()
    if list(str(div)) != num:
        continue
    print(div)
    for some in str(div):
        divided = int(some)

        # Function for telling the distance between the coordinates
'''



'''
[:]
[:1] [1:], [:2] [2:], [:3] [3:]..
[:1] [1:2] [2:], [:1] [1:3] [3:]

-
1, 2, 3, 4, 5, 6, 7...
1 2, 1 3, 1 4, 1 5,... 2 3, 2 4, 2 5...
1 2 3, 1 2 4, 1 2 5,... 2 3 4, 2 3 5, 2 3 6...

'''


"""
'''FILL OUT A LIST (ENTIRE STALLS)'''
stall = [0 for a in range(S)]
for fi in occupied:
    stall[fi - 1] = 1
print(stall)

'''GET ONLY THE ONES FROM THE LIST'''
ones = []
part = []
for div in range(0, len(stall)):
    if stall[div] == 1:
        part.append(1)
    else:
        if part != []:
            ones.append(part)
            part = []

'''FIND ALL POSSIBLE GROUPS'''
"""

fout.write(str(sum(diff) + counting + 1) + '\n')
fout.close()