"""
1
2
3 6
10 8
0 1
"""


def boolean(b1, b2):
    if b1 == b2:
        return False
    else:
        return True


def solve(N, h, a, t):
    # Forming pairs
    possibleAnswers = [0, None]
    for ind in range(N):
        for ind2 in range(ind + 1, N):
            deltaH = h[ind] - h[ind2]  # Change in height
            deltaA = a[ind2] - a[ind]  # Change in time
            import math

            try:
                date = (deltaH / deltaA)
            except ZeroDivisionError:
                if deltaH > 0:
                    if t[ind] > t[ind2]:
                        return -1
                    else:
                        continue
                elif deltaH == 0:
                    return -1
                else:
                    if t[ind] > t[ind2]:
                       continue
                    else:
                        return -1

            if boolean((t[ind] > t[ind2]), (deltaA < 0)):
                # Right-hand side must be greater
                if date == int(date):
                    date += 1
                lhs = math.ceil(date)
                possibleAnswers[0] = max(possibleAnswers[0], lhs)
            else:
                # Left-hand side must be greater
                if date == int(date):
                    date -= 1
                rhs = math.floor(date)
                if possibleAnswers[1] == None:
                    possibleAnswers[1] = rhs
                else:
                    possibleAnswers[1] = min(possibleAnswers[1], rhs)
    if possibleAnswers[1] == None:
        return possibleAnswers[0]
    elif possibleAnswers[1] >= possibleAnswers[0]:
        return possibleAnswers[0]
    else:
        return -1


T = int(input())
for i in range(0, T):
    N = int(input())
    h = list(map(int, input().split()))  # Initial height
    a = list(map(int, input().split()))  # Growing height
    t = list(map(int, input().split()))  # FJ's expectation
    print(solve(N, h, a, t))
