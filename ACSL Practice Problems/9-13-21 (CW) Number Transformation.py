"""
124987 2 3
540670 3 9
7145042 2 8
124987 2 523
4386709 1 2

4318762 4 3
72431685 1 7
123456789 7 8
9876543210 10 25
314159265358 8 428
"""

lines = [input().split(' '),
         input().split(' '),
         input().split(' '),
         input().split(' '),
         input().split(' ')]

# Method 1
for a in range(0, len(lines)):
    for b in range(1, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for a in range(0, len(lines)):
    line = lines[a]
    N, P, D = line[0], line[1], line[2]
    N = N[::-1]
    digit = int(N[P - 1])

    if 0 <= digit <= 4:
        digit += D
        digit = str(digit)
        digit = digit[-1]
    elif 5 <= digit <= 9:
        digit = str(abs(digit - D))
        if len(digit) != 1:
            digit = int(digit[0])

    N_lst = []
    for b in range(0, len(N)):
        N_lst.append(N[b])
    N_lst[P - 1] = digit

    for b in range(0, P - 1):
        N_lst[b] = '0'
    N_lst = N_lst[::-1]

    N_f = ''
    for b in range(0, len(N_lst)):
        N_f += str(N_lst[b])
    print(N_f)

print('')


# Method 2
for a in range(0, len(lines)):
    for b in range(0, len(lines[a])):
        lines[a][b] = int(lines[a][b])

for a in range(0, len(lines)):
    line = lines[a]
    N, P, D = line[0], line[1], line[2]

    quotient = str(N // 10 ** P)  # Numbers before position P
    remain = str(N % 10 ** P)  # Numbers after position P

    # Add/Subtract the digit num with D
    digit = int(remain[0])
    if 0 <= digit <= 4:
        digit += D
        digit = str(digit)
        digit = digit[-1]
    elif 5 <= digit <= 9:
        digit = str(abs(digit - D))
        if len(digit) != 1:
            digit = int(digit[0])

    num = 10 ** (P - 1)
    digit = str(int(digit) * num)
    quotient += digit
    print(quotient)
