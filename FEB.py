"""
4
BEEF

9
FEBFEBFEB

10
BFFFFFEBFE
"""


# 0 is B, 1 is E
def changeF(string, binary):
    binInd = 0
    for i in range(len(string)):
        if string[i] == 'F':
            if binary[binInd] == '0':
                string[i] = 'B'
            else:
                string[i] = 'E'
            binInd += 1
    return string


def checkExcitement(string):
    excitement = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            excitement += 1
    return excitement


N = int(input())
S = list(input())
totalCases = []  # Rising excitement
numberF = S.count('F')
counting = 1
for n in range(2 ** numberF):
    counting += 1
    '''
    order = ('0' * (numberF - len(bin(n)[2:]))) + bin(n)[2:]
    converted = changeF(S.copy(), order)
    checkedExcite = checkExcitement(converted)
    if checkedExcite not in totalCases:
        totalCases.append(checkedExcite)'''
totalCases.sort()
print(counting)

# Output
print(len(totalCases))
for fin in totalCases:
    print(fin)
