# Convert the decimal number to a different type depending on the input base
def convertDec(num, base):
    num, base = int(num), int(base)
    quotient = -1
    remainLst = []
    while quotient != 0:
        # Keep dividing the quotient with base number
        quotient = num // base
        # Keep all the remainders (converted digits) in the remainLst
        remainder = num % base
        print(f"{num} ÷ {base} = {quotient} ... {remainder}")
        remainLst.append(remainder)
        num = quotient
    remainLst.reverse()
    return remainLst


# Convert the binary number to a different type depending on the input base
def convertBinGroups(num, base):
    groups = []
    num = num[::-1]  # Reverse the string
    group, divisor = "", 0

    # Determine how the groups are divided depending on the input base
    if base == "8":
        divisor = 3
    elif base == "10":
        divisor = len(num)
    elif base == "16":
        divisor = 4

    # Divide the binary number into groups
    for g in range(0, len(num)):
        group += num[g]
        # Append the string for every three digits of binary number
        if (g + 1) % divisor == 0:
            groups.append(group)
            group = ""
    if group != "":  # Append the rest of the string group
        groups.append(group)

    # Re-reverse the order of string and list
    groups.reverse()
    for rev in range(0, len(groups)):
        groups[rev] = groups[rev][::-1]
    return groups


# Convert grouped binary numbers to a different type depending on the input base
def convertBinGroupsDifferent(num):
    # Run the for loop for each group in the list
    finalStr = ""
    for gr in range(0, len(num)):
        numConv = []
        # Convert each digit
        for dig in range(0, len(num[gr])):
            groupCon = int(num[gr][dig]) * 2 ** (len(num[gr]) - (dig + 1))  # Converted number
            print(f"{num[gr][dig]} x 2 ** {(len(num[gr]) - (dig + 1))} = {groupCon}")  # This print statement shows the process of conversion
            numConv.append(groupCon)

        # Add the converted numbers in numConv together
        digit = 0
        display = ""
        for ad in range(0, len(numConv)):
            digit += numConv[ad]
            display += str(numConv[ad])
            if ad != len(numConv) - 1:
                display += " + "
        display += f" = {digit}"
        print(display)
        print(f"Group Converted: {digit}")
        if digit >= 10 and final == "16":
            digit = chr(digit + 55)
            print(f"-> {digit}")
        finalStr += str(digit)
    return finalStr


# Convert a list to a string by adding all list elements onto an empty list
def makeOneString(lst, space):
    string = ""
    for ap in range(0, len(lst)):
        string += str(lst[ap])
        if ap != len(lst) - 1:
            string += " " * space
    return string


# Add extra zeros in front of the binary number
def addExtraZero(lst, base):
    base, length = int(base), 0
    if base == 8:
        length = 3
    elif base == 16:
        length = 4
    for z in range(1, len(lst)):
        space = length - len(lst[z])
        lst[z] = "0" * space + lst[z]
    return lst


# Numbers included for each base
two = ['0', '1']
eight = ['0', '1', '2', '3', '4', '5', '6', '7']
ten = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sixteen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']

run = True  # This variable determines whether the user wants to rerun the program again
while run == True:
    # INPUT PROCESS
    # Get the initial number's base
    initial = str(input("Initial Number Base: "))
    while initial != "2" and initial != "8" and initial != "10" and initial != "16":
        # Repeats the loop until the user puts the valid base number
        print("\nWrong input. Please enter a valid number.")
        initial = str(input("Initial Number Base: "))
    print("")

    # Get the final number's base (after conversion)
    final = str(input("Final Number Base: "))
    while True:
        # Repeats the loop until the user puts the valid base number
        if final == initial:  # If the final and initial base numbers are the same
            print("\nPlease enter a different number base.")
            final = str(input("Final Number Base: "))
        if final != "2" and final != "8" and final != "10" and final != "16":  # If the final base number is not valid
            print("\nWrong input. Please enter a valid number.")
            final = str(input("Final Number Base: "))
        if final == "2" or final == "8" or final == "10" or final == "16":
            if final != initial:
                break  # Break the loop if the final base number is valid
    print("")

    # Get the number the user wants to convert
    number = str(input("Number: "))
    passLoop = False
    baseType = 0
    while passLoop == False:
        # The if statements chooses the correct base number digits to compare
        if initial == '2':
            baseType = two
        elif initial == '8':
            baseType = eight
        elif initial == '10':
            baseType = ten
        elif initial == '16':
            baseType = sixteen
        for test in range(0, len(number)):
            # The for loop checks if the input has the correct digits for the initial type
            if number[test] not in baseType:
                print("\nPlease enter a number with right type.")
                number = str(input("Number: "))
                passLoop = False
                break
            else:
                passLoop = True
    print("")

    # TRANSLATION PROCESS
    output = ""
    print("\n----------------------------------------")  # Divisor
    # State the conversion
    initialStr, finalStr = '', ''
    if initial == '2':
        initialStr = 'Binary'
    elif initial == "8":
        initialStr = "Octal"
    elif initial == '10':
        initialStr = "Decimal"
    elif initial == "16":
        initialStr = "Hexadecimal"

    if final == '2':
        finalStr = "Binary"
    elif final == '8':
        finalStr = "Octal Decimal"
    elif final == "10":
        finalStr = "Decimal"
    elif final == "16":
        finalStr = "Hexadecimal"
    print(f"{initialStr} to {finalStr} Process:")

    # Translate the number
    if initial == '2':  # If the initial type is binary
        # This function divides the binary number into groups
        binDiv = convertBinGroups(number, final)
        for dis in range(0, len(binDiv)):
            print(binDiv[dis], end=" ")
        print("\n")
        # This function converts the binary groups into the respective type
        output = convertBinGroupsDifferent(binDiv)
    elif initial == '10':  # If the initial type is decimal
        # Convert the decimal number into another type and make it into one single string
        converted = convertDec(number, final)
        convertStr = makeOneString(converted, 0)
        # Set it for the output
        output = convertStr
    else:  # If the initial type is octal or hex
        # Determine the conversion depending on the final base
        number = number.upper()
        # Convert the letters to numbers if the digit is in hex
        newNum = []
        for h in range(0, len(number)):
            if ord("A") <= ord(number[h]) <= ord("F"):  # If the number is letter
                newNum.append(str(ord(number[h]) - 55))  # Convert it to number
            else:
                newNum.append(number[h])  # Just append without any change
        if initial == "16":
            print(makeOneString(newNum, 1))
        print("")

        # Change each number to a binary number
        for bi in range(0, len(newNum)):
            print(f"Convert {newNum[bi]} to a binary number: ")
            newNum[bi] = convertDec(newNum[bi], 2)
            newNum[bi] = makeOneString(newNum[bi], 0)
            print(newNum[bi])
        newNum = addExtraZero(newNum, initial)
        if final == "2":  # If the final base is binary
            output = makeOneString(newNum, 0)
        else:  # If the final base is not binary
            print(f"Converted to Binary: {makeOneString(newNum, 1)}")
            # Convert the number to the number with final base type
            regrouped = []
            print("")
            print(makeOneString(newNum, 1))
            # Octal to Hex or Octal to Hex
            if initial == '8' and final == '16' or initial == '16' and final == '8':
                regrouped = convertBinGroups(makeOneString(newNum, 0), final)
            elif final == '10':  # Octal/Hex to Decimal
                print(makeOneString(newNum, 0))
                regrouped = [makeOneString(newNum, 0)]
            print("")
            output = convertBinGroupsDifferent(regrouped)

    print(f"\nConverted: {output}")
    print("----------------------------------------\n\n")  # Divisor
    # Allows the user to continue/exit the running code
    askConti = ""
    while askConti != "1" and askConti != "2":
        print("Continue using the number converter?")
        print("Yes: 1\nNo: 2")
        askConti = str(input("Type a number here: "))
        if askConti == "1":
            print("\n")
            break
        elif askConti == "2":
            print("\nGood bye :)")
            run = False
            break
        else:
            print("")
            print("Please enter a valid input.")