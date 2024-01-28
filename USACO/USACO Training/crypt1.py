"""
ID: ldoyun81
LANG: PYTHON3
TASK: crypt1
"""


def getDigitNumbers(digitN, maxInd):
    digit = []
    for d in range(int('1' * digitN), int('9' * digitN)):
        less = 0
        for check in range(len(str(d))):
            if 0 < int(str(d)[check]) <= maxInd:
                less += 1
        if less == len(str(d)):
            digit.append(d)
    return digit

# Input
fin = open("crypt1.in", 'r')
fout = open('crypt1.out', 'w')

inp = fin.read().strip().split('\n')
N, digits = int(inp[0]), inp[1].split(' ')
# digits = [int(digits[i]) for i in range(len(digits))]

'''FORM ALL THE POSSIBLE NUMBERS'''
three = getDigitNumbers(3, N)  # Three-digit number
two = getDigitNumbers(2, N)  # Two-digit number

'''USE THE DIGITS TO GET ALL THE POSSIBLE NUMBERS'''
possible = 0
for d3 in three:
    for d2 in two:
        # Get 3-digit number and 2-digit number
        digit3, digit2 = list(str(d3)), list(str(d2))
        digit3, digit2 = [int(digit3[d]) - 1 for d in range(len(digit3))], [int(digit2[d]) - 1 for d in range(len(digit2))]
        num3Lst, num2Lst = [digits[digit3[d]] for d in range(len(digit3))], [int(digits[digit2[d]]) for d in range(len(digit2))]
        num3 = int(''.join(num3Lst))
        # print(num3, num2Lst)

        # Multiplication
        numbers = []  # First M, Second M, & Result
        for m in num2Lst:
            multiply = num3 * m
            numbers.append(multiply)
        numbers = [str(n) for n in numbers]

        # Check
        bool1 = len(numbers[0]) == len(numbers[1]) == 3
        bool2 = (set(numbers[0]) <= set(digits)) and (set(numbers[1]) <= set(digits))
        if bool1 and bool2:
            result = int(numbers[0]) + int(numbers[1]) * 10
            if (len(str(result)) == 4) and (set(str(result)) <= set(digits)):
                possible += 1

# print(possible)

# Output
fout.write(f"{possible}\n")
fout.close()