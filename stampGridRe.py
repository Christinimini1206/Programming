"""
4

2
**
*.
1
*

3
.**
.**
***
2
.*
**

3
...
.*.
...
3
.*.
...
...

3
**.
.**
..*
2
.*
*.
"""


def solve():
    n = int(input())
    for testCase in range(n):
        grid, stamp = initialize()
        if is_reachable(grid, stamp):
            print("YES")
        else:
            print("NO")


def initialize():
    input()
    lst = [[], []]
    for i in range(2):
        for ii in range(int(input())):
            lst[i].append(input())
    return lst[0], lst[1]


def is_reachable(grd, stp):
    empty = [['.'] * len(grd)] * len(grd)
    num = len(grd[0]) - len(stp[0]) + 1
    for r in range(num):  # Sliding vertically
        for w in range(num):  # Sliding horizontally
            # Getting the part of the grid to be tested
            part = []
            indices = []
            for gr in range(len(stp)):
                string = ''
                for gc in range(len(stp)):
                    string += grd[gr + r][gc + w]
                    indices.append([gr + r, gc + w])
                part.append(string)
            # Rotate the part and check if the stamp could be used
            rot = part
            for rotate in range(4):
                rot = [i[::-1] for i in zip(*rot)]
                # Go through each point on the part
                new = checking(rot, stp, empty, indices)
                if new != empty:
                    empty = new
                    break
            print(empty)
    return True


def checking(part, stp, empG, ind):
    for ir in range(len(part)):
        for ii in range(len(part)):
            point = part[ir][ii]
            stpP = stp[ir][ii]
            if not (point == '.' and stpP == '*'):
                for fill in ind:
                    empG[fill[0]][fill[1]] = '*'
    return empG


solve()