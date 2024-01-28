"""
4
2 spots firebreathing
0
1 flying
2 telepathic flying
"""

'''
1. Note the depth of the tree with the number of characteristics
2. Make a list of 4 elements and count the each characteristics
- [0, 0, 0, 0, 0] -> +1 to each characteristics
3.
'''

# Input
N = int(input())
lst = []
for a in range(N):
    num, *traits = input().split(' ')
    for t in range(int(num)):
        lst.append(traits[t])

# Find traits
totalTraits = set(lst)
print(totalTraits)

#
group = []
for i in range(N):
    for n in range(i, N):
        print(i, n)
'''
for t in range(len(traitLst)):
    num = int(traitLst[t][0])
    for lst in range(1, num + 1):
        chara = traitLst[t][lst]
        if chara not in traits:
            traits.append(chara)
print(traits)
'''


s = "apple"
t = set(s)
print(t)