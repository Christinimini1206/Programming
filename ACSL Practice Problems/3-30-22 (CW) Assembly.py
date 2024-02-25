import time
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

A, B, C = 0, 0, 0
ACC = 0
lst1, lst2 = lines[0], lines[1]
# Set the LOC
for loc in range(0, len(lst1)):
    if lst1[loc][0] == 'A':
        A = lst1[0][-1]
    elif lst1[loc][0] == 'B':
        B = lst1[1][-1]
    elif lst1[loc][0] == 'C':
        C = lst1[2][-1]
# Run the code
for run in range(0, len(lines[1])):
    opcode = lst2[run]
    # Add
    if opcode[0] == 'ADD':
        if opcode[-1] == 'A':
            A += ACC
            ACC = A
        elif opcode[-1] == 'B':
            B += ACC
            ACC = B
        elif opcode[-1] == 'C':
            C += ACC
            ACC = C
    # Subtract
    elif opcode[0] == 'SUBTRACT':
        if opcode[-1] == 'A':
            ACC -= A
        elif opcode[-1] == 'B':
            ACC -= B
        elif opcode[-1] == 'C':
            ACC -= C
    # Multiply
    elif opcode[0] == 'MULT':
        if opcode[-1] == 'A':
            A *= ACC
            ACC = A
        elif opcode[-1] == 'B':
            B *= ACC
            ACC = B
        elif opcode[-1] == 'C':
            C *= ACC
            ACC = C
    # Divide
    elif opcode[0] == 'DIV':
        if opcode[-1] == 'A':
            A = ACC // A
            ACC = A
        elif opcode[-1] == 'B':
            B = ACC // B
            ACC = B
        elif opcode[-1] == 'C':
            C = ACC // C
            ACC = C
    # End
    elif opcode[0] == 'END':
        break
    # Print
    elif opcode[0] == 'PRINT':
        if opcode[-1] == 'A':
            print(A)
        elif opcode[-1] == 'B':
            print(B)
        elif opcode[-1] == 'C':
            print(C)
    # Store
    elif opcode[0] == 'STORE':
        if opcode[-1] == 'A':
            A = ACC
        elif opcode[-1] == 'B':
            B = ACC
        elif opcode[-1] == 'C':
            C = ACC
    # Load
    elif opcode[0] == 'LOAD':
        if opcode[-1] == 'A':
            ACC = A
        elif opcode[-1] == 'B':
            ACC = B
        elif opcode[-1] == 'C':
            ACC = C
    print(A, B, C, ACC, 'asdf')
