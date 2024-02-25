import time
"""
30, 10, 5, 3, 2, 151
26, 2, 4, 8, 10, 50

16, 8, 4, 2, 1, 40
12, 5, 7, 4, 3, 7
8, 13, 5, 9, 4, 27
6, 21, 15, 7, 3, 18
23, 3, 16, 5, 20, 4
25, 5, 10, 15, 20, 0
8, 6, 14, 7, 20, 24
9, 13, 17, 24, 6, 52
5, 9, 18, 3, 12, 21
4, 12, 14, 6, 3, 4
"""

# Input
lines = []
for a in range(0, 10):
    lines.append(input().split(', '))
    '''for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])'''

# Run each line
for run in range(0, len(lines)):
    line = lines[run]
    nums, fNum = line[0:5], line[5]
    order = [[1, 2, 3],
             [1, 3, 2],
             [2, 1, 3],
             [2, 3, 1],
             [3, 1, 2],
             [3, 2, 1]]
    # Create different combinations of operation
    combinations = []
    operations = ['-', '*', '/', '+']
    for comb in range(0, 4):
        # Pop the last operation & put it in the front
        oper = operations.pop()
        operations.insert(0, oper)
        for arrange in range(0, 6):
            threeOper, orderOper = operations[1:], order[arrange]
            newLst = [oper, threeOper[orderOper[0] - 1], threeOper[orderOper[1] - 1], threeOper[orderOper[2] - 1]]
            combinations.append(newLst)
    finalN = 0
    # Test different combinations of operation for the numbers
    for operate in range(0, len(combinations)):
        testOper = combinations[operate]
        finaN = 0
        for letters in range(0, len(testOper)):
            # Operation +
            if testOper[letters] == '+':
                if letters == 0:
                    finalN = int(nums[letters]) + int(nums[letters + 1])
                else:
                    finalN += int(nums[letters + 1])
            # Operation -
            elif testOper[letters] == '-':
                if letters == 0:
                    finalN = int(nums[letters]) - int(nums[letters + 1])
                else:
                    finalN -= int(nums[letters + 1])
            # Operation *
            elif testOper[letters] == '*':
                if letters == 0:
                    finalN = int(nums[letters]) * int(nums[letters + 1])
                else:
                    finalN *= int(nums[letters + 1])
            # Operation /
            elif testOper[letters] == '/':
                if letters == 0:
                    finalN = int(nums[letters]) / int(nums[letters + 1])
                else:
                    finalN /= int(nums[letters + 1])
        finalN = round(finalN, 1)
        if finalN == float(fNum):
            # Create the formula
            numComb = ''
            for form in range(0, len(operations)):
                numComb += nums[form]
                numComb += ' '
                numComb += testOper[form]
                numComb += ' '
            numComb += nums[-1]
            print(numComb + ' = ' + str(fNum))
            break


