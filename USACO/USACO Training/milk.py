"""
ID: ldoyun81
LANG: PYTHON3
TASK: milk
"""

'''INPUT'''
fin = open("milk.in", 'r')
fout = open('milk.out', 'w')

inp = fin.read().strip().split('\n')
inp = [inp[ind].split(' ') for ind in range(0, len(inp))]

# Convert the strings to integers
for l in range(0, len(inp)):
    for i in range(2):
        inp[l][i] = int(inp[l][i])

total, farmers = inp[0], inp[1:]
totalUnit, numFarm = total[0], total[1]

'''SORT THE FARMERS ACCORDING TO THE PRICING'''
farmers.sort()

'''USE FOR LOOP TO CALCULATE THE MINIMUM AMOUNT OF MONEY USED'''
unitAdded, cost = 0, 0
for m in range(numFarm):
    price, unitsAva = farmers[m][0], farmers[m][1]
    for ad in range(0, unitsAva):
        if unitAdded == totalUnit:
            break
        else:
            cost += price
            unitAdded += 1

fout.write(str(cost) + '\n')
fout.close()