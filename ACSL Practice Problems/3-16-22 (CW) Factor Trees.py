"""
20
39
48
75
100
5
25
81
15
2

144
36
225
7
72
1024
500
97
4
2310
"""

lines = []
for a in range(0, 10):
    lines.append(int(input()))

for run in range(0, len(lines)):
    num = lines[run]
    print(num)
    # Calculate all the prime numbers <= input
    primes = []
    for prime in range(2, num + 1):
        divisible = 0
        for divP in range(2, prime):
            if prime % divP == 0:
                divisible += 1
        if divisible == 0:
            primes.append(prime)
        elif divisible == 1 and prime == divP:
            primes.append(prime)

    # Find prime factors for input
    pFactors = []
    if num not in primes:  # If the number has prime factors
        while num not in primes:
            for factor in range(0, len(primes)):
                if num % primes[factor] == 0:
                    num /= primes[factor]
                    pFactors.append(primes[factor])
                    # Make the prime factor tree
                    fStr = str(int(num))
                    pFactors.sort(reverse=True)
                    for string in range(0, len(pFactors)):
                        fStr += ' x '
                        fStr += str(pFactors[string])
                    print(fStr)
                    break
        pFactors.insert(-1, num)
        # Each numbers
        numbers = []
        for nums in range(0, len(pFactors)):
            if pFactors[nums] not in numbers:
                numbers.append(int(pFactors[nums]))
        numbers.sort(reverse=True)
        # Count the numbers
        simple = ''
        for cNum in range(0, len(numbers)):
            counting = numbers[cNum]
            length = pFactors.count(counting)
            simple += str(numbers[cNum])
            if length > 1:
                simple += ' ^ '
                simple += str(length)
            if cNum < len(numbers) - 1:
                simple += ' x '
        print(simple)
    else:  # If the number itself is a prime factor
        print(num)
    print()

