"""
ID: ldoyun81
LANG: PYTHON3
TASK: namenum
"""
# Input
fin = open("namenum.in", 'r')
fout = open('namenum.out', 'w')
import itertools
"""
- Get the input as a string and separate them into digits
    - Store the letters in lists: set2 = [A, B, C]
- Write all the 12 for loops for the maximum number of possible generated
names
    - Make the for loops that are not matching the number of digits skip
    - When generating the name, if the name that is in the list of given
    dictionary, put it in the empty list
- Print each name in the list as the output
"""


def makeComparisonWithLetters(name, numInd, letInd):
    # name: The list of split digits
    # numInd: The digit that is being converted
    # letInd: The location of the letter that is used for converting
    letInd += 1
    n = setLet[int(name[numInd]) - 2][letInd]
    return [n, letInd]


nameN = fin.read().strip()

fextra = open("dict.txt", "r")
dictName = set(fextra.read().split('\n'))

# Separate the input into digits
nameSpl = list(nameN)

# Convert the numbers into possible name
setLet = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"],
          ["M", "N", "O"], ["P", "R", "S"], ["T", "U", "V"], ["W", "X", "Y"]]

# Using itertools
newLetterSet = []
for a in nameSpl:
    newLetterSet.append(setLet[int(a) - 2])
# print(newLetterSet)
n = list(itertools.product(*newLetterSet))

validNames = []

for s in n:
    nameStr = ''.join(s)
    if nameStr in dictName:
        validNames.append(nameStr)

# Using for loop
"""
for t1 in range(0, 3):
    change1 = makeComparisonWithLetters(nameSpl, 0, indexLet[0])
    con1 = change1[0]
    indexLet[0] = change1[1]
    if indexLet[0] == 2:  # If the letter list index reached the limit
        indexLet[0] = -1
    if len(nameN) == 1:  # If the name is only # long
        print(con1)
        continue

    for t2 in range(0, 3):
        change2 = makeComparisonWithLetters(nameSpl, 1, indexLet[1])
        con2 = change2[0]
        indexLet[1] = change2[1]
        if indexLet[1] == 2:  # If the letter list index reached the limit
            indexLet[1] = -1
        if len(nameN) == 2:  # If the name is only # long
            print(con1, con2)
            continue

        for t3 in range(0, 3):
            change3 = makeComparisonWithLetters(nameSpl, 2, indexLet[2])
            con3 = change3[0]
            indexLet[2] = change3[1]
            if indexLet[2] == 2:  # If the letter list index reached the limit
                indexLet[2] = -1
            if len(nameN) == 3:  # If the name is only # long
                print(con1, con2, con3)
                continue

            for t4 in range(0, 3):
                change4 = makeComparisonWithLetters(nameSpl, 3, indexLet[3])
                con4 = change4[0]
                indexLet[3] = change4[1]
                if indexLet[3] == 2:  # If the letter list index reached the limit
                    indexLet[3] = -1
                if len(nameN) == 4:  # If the name is only # long
                    print(con1, con2, con3, con4)
                    continue

                for t5 in range(0, 3):
                    change5 = makeComparisonWithLetters(nameSpl, 4, indexLet[4])
                    con5 = change4[0]
                    indexLet[4] = change4[1]
                    if indexLet[4] == 2:  # If the letter list index reached the limit
                        indexLet[4] = -1
                    if len(nameN) == 5:  # If the name is only # long
                        print(con1, con2, con3, con4, con5)
                        continue

                    for t6 in range(0, 3):
                        change5 = makeComparisonWithLetters(nameSpl, 5, indexLet[5])
                        con5 = change4[0]
                        indexLet[5] = change4[1]
                        if indexLet[5] == 2:  # If the letter list index reached the limit
                            indexLet[5] = -1
                        if len(nameN) == 6:  # If the name is only # long
                            print(con1, con2, con3, con4, con5, con6)
                            continue
"""

# Combine the output into one string
finalStr = ""
for o in validNames:
    finalStr += o + "\n"

if finalStr == '':
    finalStr = "NONE\n"

print(finalStr)

fout.write(finalStr)
fout.close()

"""
Execution error: Your program (`namenum') used more than
the allotted runtime of 1 seconds (it ended or was stopped at
1.394 seconds) when presented with test case 3. It used 17660 KB
of memory. 
"""