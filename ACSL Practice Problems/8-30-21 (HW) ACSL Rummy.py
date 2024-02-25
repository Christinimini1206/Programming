"""
8H, 8C, 8S, 2C, 7S, 9H, KD
3S, 4S, TD, 9S, KC, 5S, 6S
KS, JS, KH, JH, KC, JC, 6D
5H, TD, 6H, JD, 7H, QD, 3C
2C, 2D, 4S, 6C, 7H, 7S, 8C

AH, 2H, 3H, 4H, 7S, TC, 9H
3S, QC, 8H, 4H, 8D, 4C, 8C
5S, QS, 9C, 5H, TS, 5C, JS
2S, 7D, 5H, JS, 9C, TH, 3C
2S, 9D, 9S, 2H, 9C, 2C, 9H
"""


def createSets(lst):
    lstNum = []
    repeat = []
    set = []

    for a in range(0, len(lst)):
        num = lst[a][0]
        if num not in lstNum:
            lstNum.append(num)
    for a in range(0, len(lstNum)):
        repeat.append([])

    for a in range(0, len(lstNum)):
        N = lstNum[a]
        for b in range(0, len(lst)):
            if N == lst[b][0]:
                repeat[a].append(N)

    for a in range(0, len(repeat)):
        if len(repeat[a]) >= 3:
            for b in range(0, len(lst)):
                if lst[b][0] == repeat[a][0]:
                    set.append(lst[b])
    set.sort()
    set = set[::-1]

    '''
    for a in range(0, len(set)):
        card = ''
        card += str(set[a][0])
        card += set[a][1]
        comSet.append(card)
    '''

    return set


def createRuns(lst2):
    lst = lst2
    global setCards
    for a in range(0, len(setCards)):
        if setCards[a] in lst:
            num = lst.index(setCards[a])
            lst.pop(num)
    lst.sort()
    #print(lst)

    """
    numLst = []
    for a in range(0, len(lst)):
        numLst.append(lst[a][0])
    # print(numLst)
    '''
    for a in range(0, len(numLst) - 1):
        differ = numLst[a + 1] - numLst[a]
        if differ > 1:
            return lst[::-1]
    '''
    runs = []
    if len(setCards) == 3:
        for a in range(0, len(numLst) - 4):
            group = []
            group.append(numLst[a:a + 3])
            runs.append(group)
    else:
        for a in range(0, len(numLst) - 3):
            group = []
            group.append(numLst[a:a + 2])
            runs.append(group)
    """

    shapes = []
    for a in range(0, len(lst)):
        if lst[a][1] not in shapes:
            shapes.append(lst[a][1])

    dividedRun = []
    for a in range(0, len(shapes)):
        if len(shapes) > 1:
            dividedRun.append([])
            for b in range(0, len(lst)):
                if lst[b][1] == shapes[a]:
                    dividedRun[a].append(lst[b])
    dividedRun.sort()
    # dividedRun = dividedRun[::-1]

    for a in range(0, len(dividedRun)):
        #print(dividedRun[a])
        if len(dividedRun[a]) == 1:
            dividedRun[a] = dividedRun[a][0]
            '''
            elif len(dividedRun[a]) == 2:
                for b in range(0, len(dividedRun[a])):
                    dividedRun.append(dividedRun[a][b])
                dividedRun.pop(a)
            '''
        elif len(dividedRun[a]) > 2:
            for b in range(0, len(dividedRun[a]) - 1):
                print(dividedRun[a][b])
                print(dividedRun[a][b][0] + 1, dividedRun[a][b + 1][0])
                if dividedRun[a][b][0] + 1 != dividedRun[a][b + 1][0]:
                    for c in range(b + 1, len(dividedRun[a]) - 2):
                        print(b + 1, len(dividedRun[a]) - 1, 'asdf')
                        card = dividedRun[a].pop(c)
                        dividedRun.append(card)

    print(dividedRun)

    return


lines = [input().split(', '),
         input().split(', '),
         input().split(', '),
         input().split(', '),
         input().split(', ')]

for a in range(0, len(lines)):
    cards = lines[a]
    cardsSep = []
    # Create separated cards
    for b in range(0, len(cards)):
        cardsSep.append([])
        cardsSep[b].append(cards[b][0])
        cardsSep[b].append(cards[b][1])

    # Change cards to numerical values
    for c in range(0, len(cardsSep)):
        if ord('2') <= ord(cardsSep[c][0]) <= ord('9'):
            cardsSep[c][0] = int(cardsSep[c][0])
        else:
            if cardsSep[c][0] == 'A':
                cardsSep[c][0] = 1
            elif cardsSep[c][0] == 'T':
                cardsSep[c][0] = 10
            elif cardsSep[c][0] == 'J':
                cardsSep[c][0] = 11
            elif cardsSep[c][0] == 'Q':
                cardsSep[c][0] = 12
            elif cardsSep[c][0] == 'K':
                cardsSep[c][0] = 13
        '''
        if cardsSep[c][1] == 'S':
            cardsSep[c][1] = 1
        elif cardsSep[c][1] == 'H':
            cardsSep[c][1] = 2
        elif cardsSep[c][1] == 'C':
            cardsSep[c][1] = 3
        elif cardsSep[c][1] == 'D':
            cardsSep[c][1] = 4
        '''

    # Create Sets
    setCards = createSets(cardsSep)
    numbers = []
    # Check for different sets
    for a in range(0, len(setCards)):
        if setCards[a][0] not in numbers:
            numbers.append(setCards[a][0])

    dividedSet = []
    if len(numbers) > 1:
        for a in range(0, len(numbers)):
            dividedSet.append([])
            for b in range(0, len(setCards)):
                if setCards[b][0] == numbers[a]:
                    dividedSet[a].append(setCards[b])
        dividedSet.sort()
    else:
        dividedSet = setCards

    #print(setCards, dividedSet)

    # Create Runs
    runCards = createRuns(cardsSep)
    #print(runCards)
