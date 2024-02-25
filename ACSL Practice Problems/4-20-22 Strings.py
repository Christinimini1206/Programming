"""
LS-1/RS-1/OHIO
RC-2/LC-5/CINCINNATI
LS-1/LC-3/MC-453L/MEMORIAL

RS-4/AMERICAN
LS-2/RC-3/PROGRAMMING
MC-243L/LAKOTAEAST
LC-3/RS-2/CONTEST
MC-352L/MC-452R/JRDIVISION
"""

lines = []
# Input
for a in range(0, 3):
    lines.append(input().split('/'))

# Run the code
for run in range(0, len(lines)):
    line = lines[run]
    func, string = [], line[-1]
    # Make string to a list
    strLst = []
    for s in range(0, len(string)):
        strLst.append(string[s])
    # Divide the function with dash
    for div in range(0, len(line)):
        if '-' in line[div]:
            func.append(line[div])
    # Divide the function into letters and numbers
    for div in range(0, len(func)):
        func[div] = func[div].split('-')
    # Functions
    for funcType in range(0, len(func)):
        lst = func[funcType]
        if lst[0] == 'LS':  # Left shift
            for ls in range(0, int(lst[1])):
                strLst.pop(0)
                strLst.append('#')
        elif lst[0] == 'RS':  # Right shift
            for rs in range(0, int(lst[1])):
                strLst.pop()
                strLst.insert(0, '#')
        elif lst[0] == 'RC':  # Left circle
            for lc in range(0, int(lst[1])):
                ele = strLst.pop()
                strLst.insert(0, ele)
        elif lst[0] == 'LC':  # Right circle
            for rc in range(0, int(lst[1])):
                ele = strLst.pop(0)
                strLst.append(ele)
        elif lst[0] == 'MC':
            letter = func[funcType][1]
            s, l, x, d = int(letter[0]) - 1, int(letter[1]), int(letter[2]), letter[3]
            subStr = strLst[s:s + l]
            # Make the string into list
            subStrLst = []
            for a in range(0, len(subStr)):
                subStrLst.append(subStr[a])
            # Decide the direction
            for mL in range(0, x):
                if d == 'R':
                    ele1 = subStrLst.pop()
                    subStrLst.insert(0, ele1)
                else:
                    ele1 = subStrLst.pop(0)
                    subStrLst.append(ele1)
            # Insert the substring to the original
            for rep in range(s, s + l):
                strLst[rep] = subStrLst[rep - s]

    # Make the list into a string
    finalStr = ''
    for st in range(0, len(strLst)):
        finalStr += strLst[st]
    print(finalStr)