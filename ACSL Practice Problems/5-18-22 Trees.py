import time

"""
RECURSIVEFUNCTIONS, 1
RECURSIVEFUNCTIONS, 6
RECURSIVEFUNCTIONS, 10
RECURSIVEFUNCTIONS, 15
RECURSIVEFUNCTIONS, 18

BALTIMORE, 6
MARYLAND, 4
THIRTYYEARS, 9
MARRIOTTSRIDGE, 13
BINARYSEARCHTREE, 4
"""

# Input
lines = []
for a in range(0, 5):
    lines.append(input().split(', '))
    lines[a][-1] = int(lines[a][-1])

# Run the code
for run in range(0, len(lines)):
    line = lines[run]
    string, pos = line[0], line[1]
    # Divide the string into the list of letters until position N
    letter, binTree = [], []
    for let in range(0, pos):
        letter.append(string[let])
        binTree.append('')
    # Make the tree with the letters
    binTree[0] = letter[0]
    depthPos = 0
    for tree in range(1, len(letter)):
        position, depth = 0, 0
        depthPos = 1
        while binTree[position] != '':
            if ord(letter[tree]) <= ord(binTree[depth]):  # If the letter is less than or equal to the prevLetter
                position = 2 * depth + 1
            elif ord(letter[tree]) > ord(binTree[depth]):  # If the letter is greater than the prevLetter
                position = 2 * depth + 2
            if position >= len(binTree):  # If spaces in the tree are not enough
                # Add new spaces
                newSpaces = (position - len(binTree)) + 1
                for new in range(0, newSpaces):
                    binTree.append('')
            if binTree[position] == '':  # Places the letter in that position
                binTree[position] = letter[tree]
                break
            else:  # Continues going down
                depth = position
                depthPos += 1
            # time.sleep(0.5)
    # Determine the depth of the tree with the position
    '''lengthTree, square = len(binTree), 0
    while lengthTree > 0:
        lengthTree -= 2 ** square
        if lengthTree <= 0:
            break
        else:
            square += 1'''
    print(depthPos)
