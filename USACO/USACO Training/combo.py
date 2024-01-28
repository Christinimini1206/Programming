import itertools

"""
ID: ldoyun81
LANG: PYTHON3
TASK: combo
"""


def findAllCases(lst):
    numberComb = []
    for f in range(0, 3):
        digit = lst[f]
        ind = nums[2:N + 2].index(digit) + 2
        possible = nums[ind - 2:ind + 3]
        numberComb.append(possible)
    return numberComb


'''Input'''
fin = open("combo.in", 'r')
fout = open('combo.out', 'w')

inp = fin.read().strip().split('\n')
N = int(inp[0])
john, master = list(map(int, tuple(inp[1].split(' ')))), list(map(int, tuple(inp[2].split(' '))))

'''Create a list of numbers from (1 ~ N) * 3'''
nums = []
for t in range(0, 3):
    for n in range(1, N + 1):
        nums.append(n)

nums = nums[N - 2:N * 2 + 2]
print(nums)
if len(nums) == 1:
    nums *= 5

"""
'''Create all the possible combination of the lock'''
possible = list(combinations(nums, 3))

for a in sorted(itertools.product(nums, repeat=3)):
    print(a)
"""
'''Create all the possible tolerance from John & Master Combination'''
totalPossible = []
johnCase = findAllCases(john)  # John
masterCase = findAllCases(master)  # Master

nJ = list(itertools.product(*johnCase))
nM = list(itertools.product(*masterCase))
both = [nJ, nM]

for two in both:
    for i in two:
        totalPossible.append(i)
# print(len(set(totalPossible)))


'''
both = [johnCase, masterCase]

for c in both:
    for l in sorted(itertools.product(list(set(c)), repeat=3)):
        totalPossible.append(''.join(map(str, list(l))))
print(len(set(totalPossible)))
'''
"""
'''Test all the combinations by comparing them to John & Master Combinations'''
total = 0
for c in possible:
    comb = list(c)
    print(comb)
    # print(comb)
"""

# Output
fout.write(str(len(set(totalPossible))) + '\n')
fout.close()