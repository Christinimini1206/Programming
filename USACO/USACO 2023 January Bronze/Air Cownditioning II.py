import itertools

'''
INPUT:
2 4
1 5 2
7 9 3
2 9 2 3
1 6 2 8
1 2 4 2
6 9 1 5
'''


def getRange(lst):
    rangeLst = []
    mini, maxi = 101, -1
    for c in range(len(lst)):
        if lst[c][0] < mini:
            mini = lst[c][0]
        if lst[c][1] > maxi:
            maxi = lst[c][1]
    rangeLst.append(mini)
    rangeLst.append(maxi)
    return rangeLst


def checkRange(lstLst, cows):
    # Get the list of ranges
    totalRange = []
    lst = [lstLst, cows]
    for item in lst:
        totalRange.append(getRange(item))
    if (totalRange[0][0] <= totalRange[1][0]) and (totalRange[0][1] >= totalRange[1][1]):
        return True
    else:
        return False


def checkCostCows(cows):
    lst = [0] * 100
    for cow in cows:
        lower, upper, cooling = cow
        for i in range(lower - 1, upper):
            lst[i] += cooling
    return lst


def checkCost(acs):
    lst = [0] * 100
    for ac in acs:
        lower, upper, cooling = ac[:3]
        for i in range(lower - 1, upper):
            lst[i] += cooling
    return lst


N, M = list(map(int, input().split()))
cows = [list(map(int, input().split())) for i in range(N)]
ac = [list(map(int, input().split())) for i in range(M)]

cowCost = checkCostCows(cows)
orgcost = None
for i in range(0, M + 1):
    for ii in itertools.combinations(ac, i):
        # Check the range
        if not checkRange(ii, cows):
            continue
        # Check the temperature difference
        checkCostTemp = checkCost(ii)
        if all(ac >= cow for cow, ac in zip(cowCost, checkCostTemp)):

            cost = sum([ac[3] for ac in ii])
            if orgcost is None:
                orgcost = cost
            elif orgcost > cost:
                orgcost = cost
print(orgcost)
