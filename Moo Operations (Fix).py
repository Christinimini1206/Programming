import itertools

"""
testing = list(itertools.product(['M', 'O'], repeat=5))
for l in testing:
    print(''.join(l))
"""

N = int(input())
strings = [input() for inp in range(N)]

for string in strings:
    length = len(string) - 3
    count = None
    if "MOO" in string:
        count = 0
    elif "MOM" in string:
        count = 1
    elif "OOO" in string:
        count = 1
    elif "OOM" in string:
        count = 2
    if count is not None:
        print(length + count)
    else:
        print(-1)
