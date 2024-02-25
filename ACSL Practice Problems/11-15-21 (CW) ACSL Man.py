"""
BIT, 9, A,C,D,E,F,G,H,J,K
BITE, 10, B,A,C,D,I,T,X,Y,Z

ACSL, 8, A,D,E,F,G,H,I,J
CHICAGO, 10, A,B,C,D,E,F,G,H,I,J
ILLINOIS, 16, I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X
ALLSTAR, 14, A,B,C,D,E,F,G,H,I,J,K,L,M,N
GOOGLE, 4, G,O,L,E
"""

l1 = input().split(', ')
l2 = input().split(', ')
l3 = input().split(', ')
l4 = input().split(', ')
l5 = input().split(', ')
lines = [l1, l2, l3, l4, l5]

for a in range(0, len(lines)):
    line = lines[a]
    line[1] = int(line[1])
    line[2] = line[2].split(',')

drawn = ['  O',
         '+', '=', '[]', '=', '+',
         '  []',
         '  /', '\\']

for a in range(0, len(lines)):
    line = lines[a]
    draw = []
    string, length, letters = line[0], line[1], line[2]
    room = 0
    upperBody, legs = '', ''
    for b in range(0, length):
        if letters[b] not in string:
            if 1 <= room < 5:
                upperBody += drawn[room]
            elif room == 5:
                upperBody += drawn[room]
                draw.append(upperBody)
            elif room == 7:
                legs += drawn[room]
            elif room == 8:
                legs += drawn[room]
                draw.append(legs)
                break
            else:
                draw.append(drawn[room])
            room += 1
        string = string.replace(letters[b], '-')
        if string == '-' * len(string):
            break
    if 2 <= room < 6:
        if upperBody != '':
            draw.append(upperBody)
    if room == 7:
        if legs != '':
            draw.append(legs)

    if draw == []:
        print('NONE')
    else:
        for b in range(0, len(draw)):
            print(draw[b])
    print('')

