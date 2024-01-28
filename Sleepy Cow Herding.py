# Input: 4 7 9


def solve():
    locations = list(map(int, input().split()))
    locations.sort()
    gaps = [locations[1] - locations[0] - 1, locations[2] - locations[1] - 1]

    # Minimum Time
    # Determine the type (all adjacent, one adjacent, none adjacent)
    if (gaps[0] == 0) and (gaps[1] == 0):  # If there is no gap
        print(0)
    else:  # If there is/are gap(s)
        # One is adjacent
        if ((gaps[0] == 0) and (gaps[1] != 0)) or ((gaps[0] != 0) and (gaps[1] == 0)):
            print(2)
        else:  # No adjacent gaps
            if (gaps[0] == 1) or (gaps[1] == 1):
                print(1)
            else:
                print(2)

    # Maximum Time
    # Check the gap between each location
    print(max(gaps))


solve()