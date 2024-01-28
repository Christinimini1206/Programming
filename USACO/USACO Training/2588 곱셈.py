"""
472
385
"""

# Input
num1, num2 = int(input()), int(input())
num2Lst = list(map(int, tuple(str(num2))))

for mult in num2Lst[::-1]:
    print(num1 * mult)
print(num1 * num2)