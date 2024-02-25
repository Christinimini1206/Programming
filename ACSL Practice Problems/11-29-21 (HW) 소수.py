"""
60
100
"""

# Input
num1, num2 = int(input()), int(input())
numbers = []
allN = []
for a in range(num1, num2 + 1):
    numbers.append(a)

for a in range(2, num2 + 1):
    allN.append(a)

prime = []
for a in range(0, len(numbers)):
    divisible = 0
    for b in range(0, len(allN)):
        if allN[b] <= numbers[a]:
            if numbers[a] % allN[b] == 0:
                divisible += 1
    if divisible == 1:
        prime.append(numbers[a])

sumP = 0
for a in range(0, len(prime)):
    sumP += prime[a]

print(sumP)
print(min(prime))