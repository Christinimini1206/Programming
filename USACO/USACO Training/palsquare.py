"""
ID: ldoyun81
LANG: PYTHON3
TASK: palsquare
"""
fin = open("palsquare.in", 'r')
fout = open('palsquare.out', 'w')

"""
- Create an empty list where I can gather the numbers
- Make a for loop going from 1 to 300, inclusive
    - Check if the numbers are in the base b
    - If yes, square the number and check if the squared number is palindromic
    - If also yes, create a list [number, squared number] and append it to the empty
    list
- Print the final list
"""


def convertWithBase(num, base):
    # Conversion
    convertedN = ''
    while True:
        quotient = num // base
        remainder = num % base
        if remainder >= 10:  # Change the number to a letter if needed
            remainder = chr(ord('A') + remainder - 10)
        num = quotient
        convertedN += str(remainder)
        if quotient == 0:  # Break the loop if the conversion is done
            break
    convertedN = convertedN[::-1]
    return convertedN


# Input (the base number)
b = int(fin.readline().strip())

# numbers = []
letNum = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Go through all the numbers
for n in range(1, 300 + 1):
    converted = convertWithBase(n, b)
    convertedSqr = convertWithBase(n ** 2, b)
    # Check if it is a palindromic
    if convertedSqr == convertedSqr[::-1]:
        fout.write('{0} {1}\n'.format(converted, convertedSqr))
        # passed = converted + " " + convertedSqr
        # numbers.append(passed)

fout.close()
