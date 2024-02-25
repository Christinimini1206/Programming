"""
A DC 1
B DC 2
C DC 3
PRINT C
LOAD A
MULT C
STORE A
PRINT A
DIV B
STORE C
PRINT C
SUB A
STORE B
PRINT B
ADD A
STORE A
PRINT A
END

X DC 4
Y DC 6
LOAD X
ADD Y
STORE Z
PRINT Z
STORE X
PRINT X
MULT Y
DIV X
STORE Z
PRINT Z
SUB X
STORE Z
PRINT Z
W DC -2
DIV W
STORE Z
PRINT Z
END
"""

lines = [[], []]
inputStr = ''
# Input
for a in range(0, 50):
    inputStr = input().split(' ')
    # Classify the strings into two categories
    if len(inputStr) == 1 or len(inputStr) == 2:
        lines[1].append(inputStr)
    else:
        inputStr[-1] = int(inputStr[-1])
        lines[0].append(inputStr)
    if len(lines[1]) > 0:
        if lines[1][-1] == ['END']:
            break

nums, code = lines[0], lines[1]
# Create a dictionary
dictionary = {}
for dic in range(0, len(nums)):
    dictionary[nums[dic][0]] = nums[dic][2]

l1, l2, l3 = nums[0][0], nums[1][0], nums[2][0]
dc1, dc2, dc3 = nums[0][2], nums[1][2], nums[2][2]
loc, acc = 0, 0

for run in range(0, len(code) - 1):
    opcode, letter = code[run][0], code[run][1]
    # Run the codes
    # Determine the loc
    for chooseL in range(0, len(dictionary)):
        key = list(dictionary.keys())[chooseL]
        if letter == key:
            loc = dictionary[key]
            break
    if opcode == 'ADD':
        acc += loc
    elif opcode == 'SUB':
        acc -= loc
    elif opcode == 'MULT':
        acc *= loc
    elif opcode == 'DIV':
        acc //= loc
    elif opcode == 'END':
        break
    elif opcode == 'PRINT':
        print(loc)
    elif opcode == 'STORE':
        dictionary.update({letter: acc})
    elif opcode == 'LOAD':
        acc = loc
