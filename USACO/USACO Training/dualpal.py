"""
ID: ldoyun81
LANG: PYTHON3
TASK: dualpal
"""
fin = open("dualpal.in", 'r')
fout = open('dualpal.out', 'w')

"""
Process:
- Get input & format them
- Make a function that converts the decimal number to base 2-10
- Make a while loop to find N numbers greater than S
    - If the case matches, then count the number up -> number reaching the limit
    breaks the loop
- Create a list to gather the output numbers
- Use a for loop to run the function multiple times to test base 2-10
    - Count the number matching the case -> if the number is 2 or greater, break
    the loop and append the number to the empty list
- Output the numbers in the list
"""


def convertNumBase(num, base):
    converted = ''
    while True:
        quotient = num // base
        remainder = num % base
        num = quotient
        converted += str(remainder)
        if quotient == 0:
            break
    return converted[::-1]


line = fin.readline().strip().split(' ')
n, s = int(line[0]), int(line[1])

testN = s
passedN = []

counting = 0
while counting < n:
    testN += 1
    # Test all the bases from 2 to 10
    dual = 0
    for b in range(2, 11):
        converted = convertNumBase(testN, b)
        if converted == converted[::-1]:
            dual += 1
    if dual >= 2:
        counting += 1
        fout.write('{0}\n'.format(testN))

fout.close()
