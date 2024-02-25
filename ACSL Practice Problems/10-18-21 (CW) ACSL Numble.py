"""
9678415, 7
9678415, 6
9678415, 5
9678415, 4
2678515, 3

4361842, 7
9143675, 6
1473518, 5
8264123, 4
7439264, 3
"""


def sortStrings(str1):
    numbers = []
    for a in range(0, len(str1)):
        numbers.append(str1[a])
    numbers.sort()
    newStr = ''
    for a in range(0, len(str1)):
        newStr += numbers[a]
    newStr = newStr[::-1]
    return newStr


def stringToList(str1):
    numbers = []
    for a in range(0, len(str1)):
        numbers.append(str1[a])
    return numbers


l1 = input().split(', ')
l2 = input().split(', ')
l3 = input().split(', ')
l4 = input().split(', ')
l5 = input().split(', ')
lines = [l1, l2, l3, l4, l5]

for a in range(0, len(lines)):
    line = lines[a]
    line[1] = int(line[1])
    string, length = line[0], line[1]

    # Add all the numbers
    sumN = 0
    for b in range(0, length):
        sumN += int(string[b])
    print(sumN)

    if len(string) == length:  # The length of string and length is the same
        if sumN % 5 == 0:  # If the sum is divisible by 5
            print(sortStrings(string))
    else:  # If there's a difference in the length and the limit
        sortedStr = sortStrings(string)
        '''
        remove = len(string) - length
        stringLst = []
        for b in range(0, len(sortedStr)):
            stringLst.append(sortedStr[b])
        #for b in range(0, remove):

        
        if remove == 1:
            stringLst.remove('5')
            newString = ''
            for b in range(0, len(stringLst)):
                newString += stringLst[b]
            print(newString)
        '''
        sums = []
        for b in range(0, len(string)):
            sortedStr2 = stringToList(sortedStr)
            num = sortedStr2.pop(b)
            sum2 = 0
            print(sortedStr2)
            for c in range(0, len(sortedStr2)):
                sum2 += int(sortedStr2[c])
            sums.append([])
            sums[-1].append(sum2)
            sums[-1].append(num)
        print(sums)
        for b in range(0, len(sums)):
            if sums[b][0] % 5 != 0: