import time
"""
PETERPAN
EMMAUS
ACSL

ALLENTOWN
BOOKCASE
SCIENCELEAGUE
HEXADECIMAL
ADMINISTRATION
"""

def addSpace(lst, num):
    length = (num - len(lst)) + 1
    for a in range(0, length):
        lst.append('')
    return lst


lines = []
# Input
for a in range(0, 5):
    string = input()
    lines.append([])
    for b in range(0, len(string)):  # Create a list of separated letters
        lines[a].append(string[b])

# Run the code
for run in range(0, len(lines)):
    letters = lines[run]
    tree = [letters[0]]
    # Create a blank tree
    for let in range(1, len(letters)):
        tree.append('')
    # Fill in the tree
    ind = 0
    for fill in range(1, len(letters)):
        compInd = 0
        while tree[ind] != '':
            # print(compInd, 'asdfas')
            if ord(letters[fill]) <= ord(tree[compInd]):  # If the letter is less than or equal
                ind = 2 * compInd + 1
                if ind >= len(tree):
                    tree = addSpace(tree, ind)
                if tree[ind] == '':
                    tree[ind] = letters[fill]
                    break
                else:
                    compInd = ind
            else:  # If the letter is greater
                ind = 2 * compInd + 2
                if ind >= len(tree):
                    addSpace(tree, ind)
                if tree[ind] == '':
                    tree[ind] = letters[fill]
                    break
                else:
                    compInd = ind
            # time.sleep(0.5)
    depth, num = len(tree), 0
    while depth > 0:
        depth -= 2 ** num
        num += 1
    print(num - 1)
