import time
"""
ANSWER
INPUT
AUTHOR
ENTICE
CHAIRMEN

COMPUTER
AMERICAN
ENROLLEE
AUTOMATION
WINDOW
"""

lines = []
for a in range(0, 5):
    lines.append(input())

for run in range(0, len(lines)):
    line = lines[run]
    lstL = []
    # Split letters
    for spl in range(0, len(line)):
        lstL.append(line[spl])

    # Translate
    letter = 0
    useI = 0
    while letter < len(lstL):
        # AN, AU, & A
        if lstL[letter] == 'A':
            if lstL[letter + 1] == 'N':  # AN
                lstL[letter] = 'U'
                lstL[letter + 1] = 'N'
                letter += 2
            elif lstL[letter + 1] == 'U':  # AU
                lstL[letter] = 'O'
                lstL[letter + 1] = 'O'
                letter += 2
            elif lstL.index('A') != len(lstL) - 1:
                lstL[letter] = 'E'
        # OW & O
        elif lstL[letter] == 'O':
            if lstL[letter + 1] == 'W':
                lstL[letter] = 'O'
                lstL[letter + 1] = 'O'
                letter += 2
            else:
                lstL[letter] = 'U'
        # I
        elif lstL[letter] == 'I':
            if useI == 0:
                if letter != 0:
                    lstL[letter] = 'EE'
                    useI += 1
        # EN, E start, & E end
        elif lstL[letter] == 'E':
            if letter == len(line) - 1:
                lstL[letter] = 'E-A'
            elif lstL.index('E') == 0:
                lstL[letter] = 'I'
            else:
                if letter != len(lstL) - 1:
                    if lstL[letter + 1] == 'N':
                        lstL[letter] = 'E'
                        lstL[letter + 1] = 'E'
                        letter += 2
        # U
        elif lstL[letter] == 'U':
            lstL[letter] = 'OO'
        letter += 1

    '''
    line = line.replace('AN', 'UN')
    line = line.replace('AU', 'OO')
    if 'A' in line:
        if line.index('A') != len(line) - 1:
            line = line.replace('A', 'E')
    line = line.replace('OW', 'OO')
    line = line.replace('O', 'U')
    if 'I' in line:
        if line.index('I') != 0:
            line = line.replace('I', 'EE', 1)
    if 'EN' in line:
        if line.index('N') == len(line) - 1:
            line = line.replace('EN', 'EE')
    if 'E' in line:
        if line.index('E') == len(line) - 1:
            line = line.replace('E', 'E-A')
    if 'E' in line:
        if line.index('E') == 0:
            line = line.replace('E', 'I')
    line = line.replace('U', 'OO')
    '''
    string = ''
    for final in range(0, len(lstL)):
        string += lstL[final]
    print(string)