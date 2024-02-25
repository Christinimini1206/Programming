"""
WASHINGTON
LEE

BAILEY
MILLER
AUERBACH
MOSKOWITZ
BROWN
"""

# Input
lines = []
for a in range(0, 5):
    lines.append(input())

# Run the code
for run in range(0, len(lines)):
    line = lines[run]
    code = [line[0]]  # The first letter of the word
    disregard = ['A', 'E', 'I', 'O', 'U', 'W', 'Y']
    # Create a list without A, E, I, O, U, W, Y
    for let in range(1, len(line)):
        counted = 0
        for rem in range(0, len(disregard)):
            if line[let] == disregard[rem]:
                counted += 1
        if counted == 0:
            code.append(line[let])

    if len(code) < 4:  # If the length is less than 4
        for zero in range(0, 4 - len(code)):
            code.append(0)
    # Change the letters to numbers
    numLet = [['B', 'F', 'P', 'V'],
              ['C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'],
              ['D', 'T'],
              ['L'],
              ['M', 'N'],
              ['R']]
    for change in range(1, len(code)):
        letter = code[change]
        for nums in range(0, len(numLet)):
            for lets in range(0, len(numLet[nums])):
                numLetter = numLet[nums][lets]
                if letter == numLetter:
                    code[change] = nums + 1
    # Remove not changed ones
    newCode = [code[0]]
    for dis in range(1, len(code)):
        if type(code[dis]) == int:
            newCode.append(code[dis])
    # Remove additional ones
    finalCode = []
    for disAdd in range(0, 4):
        finalCode.append(newCode[disAdd])
    # Convert it into string
    finalStr = ''
    for string in range(0, len(finalCode)):
        finalStr += str(finalCode[string])
    print(finalStr)
